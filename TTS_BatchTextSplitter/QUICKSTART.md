# 🚀 快速开始

## ✅ 安装完成

节点已正确安装在：`custom_nodes/TTS_BatchTextSplitter/`

## 🎯 使用方法

### 1. 重启 ComfyUI

### 2. 查找节点

在ComfyUI中右键 → Add Node → 搜索：
- `TTS_BatchTextSplitter`
- 或在分类中找到：`WAS Suite` → `Text` → `TTS`

### 3. 构建工作流（只需3个节点）

```
[WAS_Text_Multiline]
        ↓ text
[TTS_BatchTextSplitter]
        ↓ text_batch
[你的TTS节点]
```

### 4. 设置参数

在 TTS_BatchTextSplitter 中：
- `split_mode`: 选择 "智能分句"
- `max_segments`: 保持 100

### 5. 运行

点击 "Queue Prompt"，观察控制台输出！

## 📊 预期效果

```
📝 TTS批处理分句完成：共 4 句
🔄 ComfyUI将自动逐句传递给下游TTS节点

第1句: 加载模型(30秒) + 推理(2秒) = 32秒
第2句: 使用缓存 + 推理(2秒) = 2秒 ✅
第3句: 使用缓存 + 推理(2秒) = 2秒 ✅
第4句: 使用缓存 + 推理(2秒) = 2秒 ✅

性能提升: 70-90% 🚀
```

## 📖 详细文档

查看 [README.md](README.md) 了解完整功能说明。

## ⚙️ TTS节点要求

你的TTS节点必须实现模型缓存：

```python
class YourTTS:
    _model_cache = None  # 类变量（重要！）
    
    def infer(self, text):
        if self._model_cache is None:
            self._model_cache = load_model()
        return self._model_cache.generate(text)
```

---

**现在开始使用吧！🎙️✨**

