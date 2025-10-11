"""
TTS_BatchTextSplitter - ComfyUI自定义节点
TTS批处理分句器 - 支持逐句流式执行

通过ComfyUI的批处理机制实现：
- 长文本自动分句
- 逐句流式执行TTS
- 模型只加载一次
- 每句独立保存音频

作者: AI Assistant
日期: 2025-10-11
版本: 1.0.0
"""

from .TTS_Streaming_Batch_Nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 导出给ComfyUI
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# 可选：web目录名称（如果有web资源）
WEB_DIRECTORY = "./web"

# 节点版本信息
__version__ = "1.0.0"

