import abc
from typing import Any, Dict
import json
import os


class BaseStorage(abc.ABC):
    """Abstract state storage.
    Allows to save and retrieve state.
    """

    @abc.abstractmethod
    def save_state(self, state: Dict[str, Any]) -> None:
        """Save state in the storage"""
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve_state(self) -> Dict[str, Any]:
        """Get state from the storage"""
        raise NotImplementedError


class JsonFileStorage(BaseStorage):
    """Implementation of a storage utilizing a local file.

    Storage format: JSON
    """

    def __init__(self, file_path: str = "state.json") -> None:
        self.file_path = file_path
        try:
            with open(file_path, "r", encoding="UTF-8") as f:
                self.local_storage = json.load(f)
        except FileNotFoundError:
            self.local_storage = {}

    def save_state(self, state: Dict[str, Any]) -> None:
        with open(self.file_path, "w+", encoding="UTF-8") as f:
            json.dump(state, f, ensure_ascii=False)

    def retrieve_state(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r") as file:
            return json.load(file)


class State:
    def __init__(self, storage: BaseStorage) -> None:
        self.storage = storage
        self.local_state = storage.retrieve_state()

    def set_state(self, key: str, value: Any) -> None:
        self.local_state[key] = value

    def get_state(self, key: str) -> Any:
        return self.local_state.get(key)
