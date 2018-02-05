# Copyright 2017 Shortest Track Company. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # noinspection PyArgumentList
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class Library(Singleton):
    """
    The Singleton object, which retrieves and holds the Config ID of the Notebook.
    """
    configuration_uuid = None
    token = None

    def set_configuration_uuid(self, configuration_uuid):
        if self.configuration_uuid:
            raise RuntimeError('The configuration_uuid is already set.')

        self.configuration_uuid = configuration_uuid

    def get_config_id(self):
        """
        Retrieves the Configuration UUID.
        :return:
        """
        if self.configuration_uuid:
            return self.configuration_uuid

        raise AttributeError('The configuration_uuid is not defined in Library.')

    def set_token(self, token):
        if self.token:
            raise RuntimeError('The token is already set.')

        self.token = token

    def get_token(self):
        """
        Retrieves the token.
        :return:
        """
        if self.token:
            return self.token
        else:
            import os
            return 'Bearer '+os.environ['ST_API_TOKEN ']
        raise AttributeError('The token is not defined in Library.')

    def read_matrix(self, matricesid, datasetsid, tablename):
        """
        Retrieves the table data.
        :return dataframe:
        """
        from st_library.dataprovider.structured_data import Table
        tbl = Table("edac25ec-25e3-4949-9f49-d42124c26bf2", "52db99d3-edfb-44c5-b97a-f09df4402081", "bbb")
        return (tbl.to_dataframe())

    def download_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        from st_library.dataprovider.unstructured_data import Item
        item = Item(datasetsid=datasetsid)
        return item.download_file(filename)

    def upload_file(self, datasetsid, filename):
        """
        Download dataset files to disk.
        :return local file path:
        """
        from st_library.dataprovider.unstructured_data import Item
        item = Item(datasetsid=datasetsid)
        return item.upload_file(filename)

    def delete_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        from st_library.dataprovider.unstructured_data import Item
        item = Item(datasetsid=datasetsid)
        return item.delete_file(filename)