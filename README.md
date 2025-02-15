<div align="center">

<img src="https://github.com/Event-AHU/XiHeFusion/blob/main/NFlogo.jpg" width="300">

**XiHeFusion: Harnessing Large Language Models for Science Communication in Nuclear Fusion, Xiao Wang, Qingquan Yang, Fuling Wang, Qiang Chen, Wentao Wu, Yu Jin, Jingtao Jiang, Liye Jin, Bo Jiang, Dengdi Sun, Wanli Lv, Meiwen Chen, Zehua Chen, Guosheng Xu, Jin Tang
arXiv Pre-print arXiv:2502.05615 [[Paper](https://arxiv.org/abs/2502.05615)]** 

------

</div>



# :dart: News 

* [2025.02.06] Demo video for XiHeFusion is available on [**Youtube**](https://youtu.be/LqV61LrvGKg?si=nu-PMBL9ZtiLJFZT), [**Bilibili**](https://www.bilibili.com/video/BV1zuKKeXEw8/?share_source=copy_web&vd_source=bd3d199c910fc6b8eadfc40413435b61) 

* [2025.01.28] XiHeFusion is released on [GitHub](https://github.com/Event-AHU/XiHeFusion) 



## Abstract 
Nuclear fusion is one of the most promising ways for humans to obtain infinite energy. Currently, with the rapid development of artificial intelligence, the mission of nuclear fusion has also entered a critical period of its development. How to let more people to understand nuclear fusion and join in its research is one of the effective means to accelerate the implementation of fusion. This paper proposes the first large model in the field of nuclear fusion, XiHeFusion, which is obtained through supervised fine-tuning based on the open-source large model Qwen2.5-14B. We have collected multi-source knowledge about nuclear fusion tasks to support the training of this model, including the common crawl, eBooks, arXiv, dissertation, etc. After the model has mastered the knowledge of the nuclear fusion field, we further used the chain of thought to enhance its logical reasoning ability, making XiHeFusion able to provide more accurate and logical answers. In addition, we propose a test questionnaire containing 180+ questions to assess the conversational ability of this science popularization large model. Extensive experimental results show that our nuclear fusion dialogue model, XiHeFusion, can perform well in answering science popularization knowledge. 


## Framework 
<img src="https://github.com/Event-AHU/XiHeFusion/blob/main/figures/XiHeFusion_framework.jpg" alt="Watch the video" width="600" align="center">


## Demo Video 
Watch the demo video below:

- **Youtube**：[https://youtu.be/LqV61LrvGKg?si=nu-PMBL9ZtiLJFZT](https://youtu.be/LqV61LrvGKg?si=nu-PMBL9ZtiLJFZT)  

- **Bilibili**：[XiHeFusion_Demo](https://www.bilibili.com/video/BV1zuKKeXEw8/?share_source=copy_web&vd_source=bd3d199c910fc6b8eadfc40413435b61) 



## Model Deployment 

1.First, configure the relevant environment according to [https://github.com/hiyouga/LLaMA-Factory ](https://github.com/hiyouga/LLaMA-Factory).

2.We provide a basic conversational demo and a programmatic demo using API calls in demo.

3.Conversational demo:

```python
#Execute 
python demo/chat_demo.py
```

4.API call execution:

```python
# Modify model_name_or_path in /examples/inference/api_inference.yaml
# Load the model and modify CUDA_VISIBLE_DEVICES API_PORT
CUDA_VISIBLE_DEVICES=2 API_PORT=8005 nohup llamafactory-cli api LLaMA-Thinks/examples/inference/api_inference.yaml &
# Execute
python demo/api_demo.py
```



### Environment Setting  

### Dataset Processing 
<img src="https://github.com/Event-AHU/XiHeFusion/blob/main/figures/data_preprocess.jpg" alt="Watch the video" width="600"> 

### Optimization Curve 
<img src="https://github.com/Event-AHU/XiHeFusion/blob/main/figures/loss_curve.jpg" alt="Watch the video" width="500"> 




## Assessment for Nuclear Fusion 

Please check the file [[**questions_for_XiHeFusion.docx**](https://github.com/Event-AHU/XiHeFusion/blob/main/questions_for_XiHeFusion.docx)] for the assessment. 


<img src="https://github.com/Event-AHU/XiHeFusion/blob/main/figures/NFAssessment.jpg" alt="Watch the video" width="800">


## Experimental Results 



## Acknowledgement 



## Citation 
```
@misc{wang2025xihefusion,
 title={XiHeFusion: Harnessing Large Language Models for Science Communication in Nuclear Fusion}, 
 author={Xiao Wang and Qingquan Yang and Fuling Wang and Qiang Chen and Wentao Wu and Yu Jin and Jingtao Jiang and Liye Jin and Bo Jiang and Dengdi Sun and Wanli Lv and Meiwen Chen and Zehua Chen and Guosheng Xu and Jin Tang},
 year={2025},
 eprint={2502.05615},
 archivePrefix={arXiv},
 primaryClass={cs.CV},
 url={https://arxiv.org/abs/2502.05615}, 
}
```



## Star History
<a href="https://star-history.com/#Event-AHU/XiHeFusion&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Event-AHU/XiHeFusion&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Event-AHU/XiHeFusion&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Event-AHU/XiHeFusion&type=Date" />
 </picture>
</a>

