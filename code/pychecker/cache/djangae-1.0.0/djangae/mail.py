# STANDARD LIB
from email.MIMEBase import MIMEBase
import logging

# THIRD PARTY
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMultiAlternatives
from google.appengine.api import mail as aeemail
from google.appengine.ext import deferred
from google.appengine.api.mail_errors import InvalidSenderError
from google.appengine.runtime import apiproxy_errors


logger = logging.getLogger(__name__)


class EmailBackend(BaseEmailBackend):
    can_defer = False

    def send_messages(self, email_messages):
        num_sent = 0
        for message in email_messages:
            if self._send(message):
                num_sent += 1
        return num_sent

    def _copy_message(self, message):
        """
        Creates and returns App Engine EmailMessage class from message.
        """
        gmsg = aeemail.EmailMessage(sender=message.from_email,
                                    to=message.to,
                                    subject=message.subject,
                                    body=message.body)
        if message.extra_headers.get('Reply-To', None):
            gmsg.reply_to = message.extra_headers['Reply-To']
        if message.cc:
            gmsg.cc = list(message.cc)
        if message.bcc:
            gmsg.bcc = list(message.bcc)
        if message.attachments:
            # Must be populated with (filename, filecontents) tuples.
            attachments = []
            for attachment in message.attachments:
                if isinstance(attachment, MIMEBase):
                    attachments.append((attachment.get_filename(),
                                        attachment.get_payload(decode=True)))
                else:
                    attachments.append((attachment[0], attachment[1]))
            gmsg.attachments = attachments
        # Look for HTML alternative content.
        if isinstance(message, EmailMultiAlternatives):
            for content, mimetype in message.alternatives:
                if mimetype == 'text/html':
                    gmsg.html = content
                    break
        return gmsg

    def _send(self, message):
        try:
            message = self._copy_message(message)
        except (ValueError, aeemail.InvalidEmailError) as err:
            logger.warn(err)
            if not self.fail_silently:
                raise
            return False
        if self.can_defer:
            self._defer_send(message)
            return True
        return self._do_send(message)

    def _do_send(self, message):
        try:
            message.send()
        except (aeemail.Error, apiproxy_errors.Error) as e:
            if isinstance(e, InvalidSenderError):
                logger.error("Invalid 'from' address: %s", message.sender)
            if not self.fail_silently:
                raise
            return False
        return True

    def _defer_send(self, message):
        queue_name = getattr(settings, 'EMAIL_QUEUE_NAME', 'default')
        deferred.defer(self._do_send, message, _queue=queue_name)


class AsyncEmailBackend(EmailBackend):
    can_defer = True
