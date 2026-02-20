# RPG Monster Generator Node Package
import importlib

# モジュール名にハイフンが含まれるため、importlib を使用して動的にインポートします
try:
    node_module = importlib.import_module(".RPG-Monster-Generator", __package__)
    NODE_CLASS_MAPPINGS = getattr(node_module, "NODE_CLASS_MAPPINGS")
    NODE_DISPLAY_NAME_MAPPINGS = getattr(node_module, "NODE_DISPLAY_NAME_MAPPINGS")
except ImportError:
    # 互換性やエラーハンドリング
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
