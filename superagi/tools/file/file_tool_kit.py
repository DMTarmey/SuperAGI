from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolKit
from superagi.tools.file.append_file import AppendFileTool
from superagi.tools.file.delete_file import DeleteFileTool
from superagi.tools.file.list_files import ListFileTool
from superagi.tools.file.read_file import ReadFileTool
from superagi.tools.file.write_file import WriteFileTool


class FileToolKit(BaseToolKit, ABC):
    name: str = "File Toolkit"
    description: str = "File Tool kit contains all tools related to file operations"

    def get_tools(self) -> List[BaseTool]:
        return [AppendFileTool(), DeleteFileTool(), ListFileTool(), ReadFileTool(), WriteFileTool()]

    def get_env_keys(self) -> List[str]:
        return [
            "RESOURCES_INPUT_ROOT_DIR",
            "RESOURCES_OUTPUT_ROOT_DIR"
            # Add more file related config keys here
        ]
