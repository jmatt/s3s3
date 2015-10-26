"""
The API for s3s3.
"""
import tempfile

from boto.s3.connection import S3Connection


def create_connection(connection_args):
    connection_args = connection_args.copy()
    connection_args.pop('bucket_name')
    return S3Connection(**connection_args)


def upload(source_key, dest_keys):
    """
    `source_key` The source boto s3 key.
    `dest_keys` The destination boto s3 keys.
    """
    # Use the same name if no destination key is passed.
    if not dest_key:
        dest_key = source_key
    with tempfile.NamedTemporaryFile() as data:
        source_key.get_contents_to_file(data)
        for dest_key in dest_keys:
            dest_key.set_contents_from_filename(data.name)
