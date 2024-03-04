# coding: utf-8
# STANDARD LIB
from unittest import skipIf
import os

# THIRD PARTY
from django.core.files.base import File, ContentFile
from django.db import models
from django.test.utils import override_settings
from django.utils import six
from google.appengine.api import urlfetch
from google.appengine.api.images import TransformationError, LargeImageError

# DJANGAE
from djangae.contrib import sleuth
from djangae.db import transaction
from djangae.storage import BlobstoreStorage, CloudStorage, has_cloudstorage
from djangae.test import TestCase


class ModelWithImage(models.Model):
    class Meta:
        app_label = "djangae"

    image = models.ImageField()


class ModelWithTextFile(models.Model):
    class Meta:
        app_label = "djangae"

    text_file = models.FileField()


@skipIf(not has_cloudstorage, "Cloud Storage not available")
class CloudStorageTests(TestCase):

    @override_settings(CLOUD_STORAGE_BUCKET='test_bucket')
    def test_basic_actions(self):
        storage = CloudStorage()
        name = u'tmp.ąćęłńóśźż.马铃薯.zip'

        f = ContentFile('content', name='my_file')
        filename = storage.save(name, f)
        self.assertIsInstance(filename, six.string_types)
        self.assertTrue(filename.endswith(name))

        self.assertTrue(storage.exists(filename))
        self.assertEqual(storage.size(filename), len('content'))
        url = storage.url(filename)
        self.assertIsInstance(url, six.string_types)
        self.assertNotEqual(url, '')

        abs_url = six.moves.urllib.parse.urlunparse(
            ('http', os.environ['HTTP_HOST'], url, None, None, None)
        )
        response = urlfetch.fetch(abs_url)
        self.assertEqual(response.status_code, six.moves.http_client.OK)
        self.assertEqual(response.content, 'content')

        f = storage.open(filename)
        self.assertIsInstance(f, File)
        self.assertEqual(f.read(), 'content')

        # Delete it
        storage.delete(filename)
        self.assertFalse(storage.exists(filename))

    @override_settings(CLOUD_STORAGE_BUCKET='test_bucket')
    def test_dotslash_prefix(self):
        storage = CloudStorage()
        name = './my_file'
        f = ContentFile('content')
        filename = storage.save(name, f)
        self.assertEqual(filename, name.lstrip("./"))

    @override_settings(CLOUD_STORAGE_BUCKET='test_bucket')
    def test_supports_nameless_files(self):
        storage = CloudStorage()
        f2 = ContentFile('nameless-content')
        storage.save('tmp2', f2)

    @override_settings(CLOUD_STORAGE_BUCKET='test_bucket')
    def test_new_objects_get_the_default_acl(self):
        storage = CloudStorage()
        filename = 'example.txt'
        fileobj = ContentFile('content', name=filename)

        with sleuth.watch('cloudstorage.open') as open_func:
            storage.save(filename, fileobj)

        self.assertTrue(storage.exists(filename))
        # There's no x-goog-acl argument, so default perms are applied.
        self.assertEqual(open_func.calls[0].kwargs['options'], {})

    @override_settings(CLOUD_STORAGE_BUCKET='test_bucket')
    def test_new_objects_with_an_explicit_acl(self):
        storage = CloudStorage(google_acl='public-read')
        filename = 'example.txt'
        fileobj = ContentFile('content', name=filename)

        with sleuth.watch('cloudstorage.open') as open_func:
            storage.save(filename, fileobj)

        self.assertTrue(storage.exists(filename))
        self.assertEqual(
            open_func.calls[0].kwargs['options'],
            {'x-goog-acl': 'public-read'},
        )

    @override_settings(
        CLOUD_STORAGE_BUCKET='test_bucket',
        DEFAULT_FILE_STORAGE='djangae.storage.CloudStorage'
    )
    def test_access_url_inside_transaction(self):
        """ Regression test.  Make sure that accessing the `url` of an ImageField can be done
            inside a transaction without causing the error:
            "BadRequestError: cross-groups transaction need to be explicitly specified (xg=True)"
        """
        instance = ModelWithImage(
            image=ContentFile('content', name='my_file')
        )
        instance.save()
        with sleuth.watch('djangae.storage.get_serving_url') as get_serving_url_watcher:
            with transaction.atomic():
                instance.refresh_from_db()
                instance.image.url  # Access the `url` attribute to cause death
                instance.save()
            self.assertTrue(get_serving_url_watcher.called)

    @override_settings(
        CLOUD_STORAGE_BUCKET='test_bucket',
        DEFAULT_FILE_STORAGE='djangae.storage.CloudStorage'
    )
    def test_get_non_image_url(self):
        """ Regression test. Make sure that if the file is not an image
            we still get a file's urls without throwing a
            TransformationError.
        """
        instance = ModelWithTextFile(
            text_file=ContentFile('content', name='my_file')
        )
        instance.save()
        with sleuth.watch('djangae.storage.six.moves.urllib.parse.quote') as urllib_quote_watcher:
            with sleuth.detonate('djangae.storage.get_serving_url', TransformationError):
                instance.refresh_from_db()
                instance.text_file.url
                instance.save()
                self.assertTrue(urllib_quote_watcher.called)

    @override_settings(
        CLOUD_STORAGE_BUCKET='test_bucket',
        DEFAULT_FILE_STORAGE='djangae.storage.CloudStorage'
    )
    def test_image_serving_url_is_secure(self):
        """ When we get a serving URL for an image, it should be https:// not http:// """
        instance = ModelWithImage(
            image=ContentFile('content', name='my_file')
        )
        instance.save()
        # Because we're not on production, get_serving_url() actually just returns a relative URL,
        # so we can't check the result, so instead we check the call to get_serving_url
        with sleuth.watch("djangae.storage.get_serving_url") as watcher:
            instance.image.url  # access the URL to trigger the call to get_serving_url
        self.assertTrue(watcher.calls[0].kwargs['secure_url'])


class BlobstoreStorageTests(TestCase):
    def test_basic_actions(self):

        storage = BlobstoreStorage()

        # Save a new file
        f = ContentFile('content', name='my_file')
        filename = storage.save('tmp', f)

        self.assertIsInstance(filename, six.string_types)
        self.assertTrue(filename.endswith('tmp'))

        # Check .exists(), .size() and .url()
        self.assertTrue(storage.exists(filename))
        self.assertEqual(storage.size(filename), len('content'))
        url = storage.url(filename)
        self.assertIsInstance(url, six.string_types)
        self.assertNotEqual(url, '')

        # Check URL can be fetched
        abs_url = six.moves.urllib.parse.urlunparse(
            ('http', os.environ['HTTP_HOST'], url, None, None, None)
        )
        response = urlfetch.fetch(abs_url)
        self.assertEqual(response.status_code, six.moves.http_client.OK)
        self.assertEqual(response.content, 'content')

        # Open it, read it
        # NOTE: Blobstore doesn’t support updating existing files.
        f = storage.open(filename)
        self.assertIsInstance(f, File)
        self.assertEqual(f.read(), 'content')

        # Delete it
        storage.delete(filename)
        self.assertFalse(storage.exists(filename))

    def test_supports_nameless_files(self):
        storage = BlobstoreStorage()
        f2 = ContentFile('nameless-content')
        storage.save('tmp2', f2)

    def test_transformation_error(self):
        storage = BlobstoreStorage()
        with sleuth.detonate('djangae.storage.get_serving_url', TransformationError):
            self.assertEqual('thing', storage.url('thing'))

    def test_large_image_error(self):
        storage = BlobstoreStorage()
        with sleuth.detonate('djangae.storage.get_serving_url', LargeImageError):
            self.assertEqual('thing', storage.url('thing'))

    def test_image_serving_url_is_secure(self):
        """ When we get a serving URL for an image, it should be https:// not http:// """
        storage = BlobstoreStorage()
        # Save a new file
        f = ContentFile('content', name='my_file')
        filename = storage.save('tmp', f)
        # Because we're not on production, get_serving_url() actually just returns a relative URL,
        # so we can't check the result, so instead we check the call to get_serving_url
        with sleuth.watch("djangae.storage.get_serving_url") as watcher:
            storage.url(filename)  # access the URL to trigger the call to get_serving_url
        self.assertTrue(watcher.calls[0].kwargs['secure_url'])
