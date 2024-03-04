import datetime
import logging
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from globus_sdk import utils
from globus_sdk.types import UUIDLike

if TYPE_CHECKING:
    import globus_sdk

log = logging.getLogger(__name__)


class TransferData(utils.PayloadWrapper):
    r"""
    Convenience class for constructing a transfer document, to use as the
    `data` parameter to
    :meth:`submit_transfer <globus_sdk.TransferClient.submit_transfer>`.

    At least one item must be added using
    :meth:`add_item <globus_sdk.TransferData.add_item>`.

    If ``submission_id`` isn't passed, one will be fetched automatically. The
    submission ID can be pulled out of here to inspect, but the document
    can be used as-is multiple times over to retry a potential submission
    failure (so there shouldn't be any need to inspect it).

    :param transfer_client: A ``TransferClient`` instance which will be used to get a
        submission ID if one is not supplied. Should be the same instance that is used
        to submit the transfer.
    :type transfer_client: :class:`TransferClient <globus_sdk.TransferClient>`
    :param source_endpoint: The endpoint ID of the source endpoint
    :type source_endpoint: str or UUID
    :param destination_endpoint: The endpoint ID of the destination endpoint
    :type destination_endpoint: str or UUID
    :param label: A string label for the Task
    :type label: str, optional
    :param submission_id: A submission ID value fetched via :meth:`get_submission_id \
        <globus_sdk.TransferClient.get_submission_id>`. Defaults to using
        ``transfer_client.get_submission_id``
    :type submission_id: str or UUID, optional
    :param sync_level: The method used to compare items between the source and
        destination. One of  ``"exists"``, ``"size"``, ``"mtime"``, or ``"checksum"``
        See the section below on sync-level for an explanation of values.
    :type sync_level: int or str, optional
    :param verify_checksum: When true, after transfer verify that the source and
        destination file checksums match. If they don't, re-transfer the entire file and
        keep trying until it succeeds. This will create CPU load on both the origin and
        destination of the transfer, and may even be a bottleneck if the network speed
        is high enough.
        [default: ``False``]
    :type verify_checksum: bool, optional
    :param preserve_timestamp: When true, Globus Transfer will attempt to set file
        timestamps on the destination to match those on the origin. [default: ``False``]
    :type preserve_timestamp: bool, optional
    :param encrypt_data: When true, all files will be TLS-protected during transfer.
        [default: ``False``]
    :type encrypt_data: bool, optional
    :param deadline: An ISO-8601 timestamp (as a string) or a datetime object which
        defines a deadline for the transfer. At the deadline, even if the data transfer
        is not complete, the job will be canceled. We recommend ensuring that the
        timestamp is in UTC to avoid confusion and ambiguity. Examples of ISO-8601
        timestamps include ``2017-10-12 09:30Z``, ``2017-10-12 12:33:54+00:00``, and
        ``2017-10-12``
    :type deadline: str or datetime, optional
    :param recursive_symlinks: Specify the behavior of recursive directory transfers
        when encountering symlinks. One of ``"ignore"``, ``"keep"``, or ``"copy"``.
        ``"ignore"`` skips symlinks, ``"keep"`` creates symlinks at the destination
        matching the source (without modifying the link path at all), and
        ``"copy"`` follows symlinks on the source, failing if the link is invalid.
        [default: ``"ignore"``]
    :type recursive_symlinks: str
    :param skip_source_errors: When true, source permission denied and file
        not found errors from the source endpoint will cause the offending
        path to be skipped.
        [default: ``False``]
    :type skip_source_errors: bool, optional
    :param fail_on_quota_errors: When true, quota exceeded errors will cause the
        task to fail.
        [default: ``False``]
    :type fail_on_quota_errors: bool, optional
    :param delete_destination_extra: Delete files, directories, and symlinks on the
        destination endpoint which don’t exist on the source endpoint or are a
        different type. Only applies for recursive directory transfers.
        [default: ``False``]
    :param delete_destination_extra: bool, optional
    :param additional_fields: additional fields to be added to the transfer
        document. Mostly intended for internal use
    :type additional_fields: dict, optional

    **Sync Levels**

    The values for ``sync_level`` are used to determine how comparisons are made between
    files found both on the source and the destination. When files match, no data
    transfer will occur.

    For compatibility, this can be an integer ``0``, ``1``, ``2``, or ``3`` in addition
    to the string values.

    The meanings are as follows:

    =====================   ========
    value                   behavior
    =====================   ========
    ``0``, ``exists``       Determine whether or not to transfer based on file
                            existence. If the destination file is absent, do the
                            transfer.
    ``1``, ``size``         Determine whether or not to transfer based on the size of
                            the file. If destination file size does not match the
                            source, do the transfer.
    ``2``, ``mtime``        Determine whether or not to transfer based on modification
                            times. If source has a newer modified time than the
                            destination, do the transfer.
    ``3``, ``checksum``     Determine whether or not to transfer based on checksums of
                            file contents. If source and destination contents differ, as
                            determined by a checksum of their contents, do the transfer.
    =====================   ========

    **Examples**

    See the
    :meth:`submit_transfer <globus_sdk.TransferClient.submit_transfer>`
    documentation for example usage.

    **External Documentation**

    See the
    `Task document definition \
    <https://docs.globus.org/api/transfer/task_submit/#document_types>`_
    and
    `Transfer specific fields \
    <https://docs.globus.org/api/transfer/task_submit/#transfer_specific_fields>`_
    in the REST documentation for more details on Transfer Task documents.

    .. automethodlist:: globus_sdk.TransferData
    """

    def __init__(
        self,
        transfer_client: "globus_sdk.TransferClient",
        source_endpoint: UUIDLike,
        destination_endpoint: UUIDLike,
        *,
        label: Optional[str] = None,
        submission_id: Optional[UUIDLike] = None,
        sync_level: Optional[str] = None,
        verify_checksum: bool = False,
        preserve_timestamp: bool = False,
        encrypt_data: bool = False,
        deadline: Optional[Union[datetime.datetime, str]] = None,
        skip_source_errors: bool = False,
        fail_on_quota_errors: bool = False,
        recursive_symlinks: str = "ignore",
        delete_destination_extra: bool = False,
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__()
        log.info("Creating a new TransferData object")
        self["DATA_TYPE"] = "transfer"
        self["submission_id"] = (
            submission_id or transfer_client.get_submission_id()["value"]
        )
        self["source_endpoint"] = str(source_endpoint)
        self["destination_endpoint"] = str(destination_endpoint)
        self["verify_checksum"] = verify_checksum
        self["preserve_timestamp"] = preserve_timestamp
        self["encrypt_data"] = encrypt_data
        self["recursive_symlinks"] = recursive_symlinks
        self["skip_source_errors"] = skip_source_errors
        self["fail_on_quota_errors"] = fail_on_quota_errors
        self["delete_destination_extra"] = delete_destination_extra
        if label is not None:
            self["label"] = label
        if deadline is not None:
            self["deadline"] = str(deadline)

        # map the sync_level (if it's a nice string) to one of the known int
        # values
        # you can get away with specifying an invalid sync level -- the API
        # will just reject you with an error. This is kind of important: if
        # more levels are added in the future this method doesn't become
        # garbage overnight
        if sync_level is not None:
            sync_dict = {"exists": 0, "size": 1, "mtime": 2, "checksum": 3}
            # TODO: sync_level not allowed to be int?
            self["sync_level"] = sync_dict.get(sync_level, sync_level)

        self["DATA"] = []

        for k, v in self.items():
            log.info("TransferData.%s = %s", k, v)

        if additional_fields is not None:
            self.update(additional_fields)
            for option, value in additional_fields.items():
                log.info(
                    f"TransferData.{option} = {value} (option passed "
                    "in via additional_fields)"
                )

    def add_item(
        self,
        source_path: str,
        destination_path: str,
        *,
        recursive: bool = False,
        external_checksum: Optional[str] = None,
        checksum_algorithm: Optional[str] = None,
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Add a file or directory to be transferred. If the item is a symlink
        to a file or directory, the file or directory at the target of
        the symlink will be transferred.

        Appends a transfer_item document to the DATA key of the transfer
        document.

        .. note::

            The full path to the destination file must be provided for file items.
            Parent directories of files are not allowed. See
            `task submission documentation
            <https://docs.globus.org/api/transfer/task_submit/#submit_transfer_task>`_
            for more details.

        :param source_path: Path to the source directory or file to be transferred
        :type source_path: str
        :param destination_path: Path to the source directory or file will be
            transferred to
        :type destination_path: str
        :param recursive: Set to True if the target at source path is a directory
        :type recursive: bool
        :param external_checksum: A checksum to verify both source file and destination
            file integrity. The checksum will be verified after the data transfer and a
            failure will cause the entire task to fail. Cannot be used with directories.
            Assumed to be an MD5 checksum unless checksum_algorithm is also given.
        :type external_checksum: str, optional
        :param checksum_algorithm: Specifies the checksum algorithm to be used when
            verify_checksum is True, sync_level is "checksum" or 3, or an
            external_checksum is given.
        :type checksum_algorithm: str, optional
        """
        item_data = {
            "DATA_TYPE": "transfer_item",
            "source_path": source_path,
            "destination_path": destination_path,
            "recursive": recursive,
            "external_checksum": external_checksum,
            "checksum_algorithm": checksum_algorithm,
        }
        if additional_fields is not None:
            item_data.update(additional_fields)

        log.debug(
            'TransferData[{}, {}].add_item: "{}"->"{}"'.format(
                self["source_endpoint"],
                self["destination_endpoint"],
                source_path,
                destination_path,
            )
        )
        self["DATA"].append(item_data)

    def add_symlink_item(self, source_path: str, destination_path: str) -> None:
        """
        Add a symlink to be transferred as a symlink rather than as the
        target of the symlink.

        Appends a transfer_symlink_item document to the DATA key of the
        transfer document.

        :param source_path: Path to the source symlink
        :type source_path: str
        :param destination_path: Path to which the source symlink will be transferred
        :type destination_path: str
        """
        item_data = {
            "DATA_TYPE": "transfer_symlink_item",
            "source_path": source_path,
            "destination_path": destination_path,
        }
        log.debug(
            'TransferData[{}, {}].add_symlink_item: "{}"->"{}"'.format(
                self["source_endpoint"],
                self["destination_endpoint"],
                source_path,
                destination_path,
            )
        )
        self["DATA"].append(item_data)
