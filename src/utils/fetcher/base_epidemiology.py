# Copyright (C) 2020 University of Oxford
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from abc import abstractmethod

__all__ = ('BaseEpidemiologyFetcher')

from utils.types import FetcherType
from utils.fetcher.abstract_fetcher import AbstractFetcher


class BaseEpidemiologyFetcher(AbstractFetcher):
    TYPE = FetcherType.EPIDEMIOLOGY
    LOAD_PLUGIN = False

    def upsert_data(self, **kwargs):
        self.data_adapter.upsert_data(self.TYPE, **kwargs)

    def get_data(self, **kwargs):
        return self.data_adapter.get_data(self.TYPE.value, **kwargs)

    def get_earliest_timestamp(self):
        return self.data_adapter.get_earliest_timestamp(self.TYPE.value, self.SOURCE)

    def get_latest_timestamp(self):
        return self.data_adapter.get_latest_timestamp(self.TYPE.value, self.SOURCE)

    def get_details(self):
        return self.data_adapter.get_details(self.TYPE.value, self.SOURCE)

    @abstractmethod
    def run(self):
        raise NotImplementedError()
