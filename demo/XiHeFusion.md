# XiHeFusion

1.First, configure the relevant environment according to [https://github.com/hiyouga/LLaMA-Factory ](https://github.com/hiyouga/LLaMA-Factory).

2.We provide a basic conversational demo and a programmatic demo using API calls.

3. Conversational demo:

```python
#Execute 
python chat_demo.py
```

4.API call execution:

```python
# Modify model_name_or_path in /examples/inference/api_inference.yaml
# Load the model and modify API_PORT
CUDA_VISIBLE_DEVICES=2 API_PORT=8005 nohup llamafactory-cli api LLaMA-Thinks/examples/inference/api_inference.yaml &
# Execute
python api_demo.py
```

