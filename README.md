<div align="center">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/pyqt_code/CTCS/resource/figure/icon.png" width="200" height="200">
</div>
<br/>
<div align="center">
  <img src="https://img.shields.io/badge/-Python-blue.svg">
  <img src="https://img.shields.io/badge/-PyQt5-green.svg">
  <img src="https://img.shields.io/badge/-Conda-orange.svg">
  <img src="https://img.shields.io/badge/-TensorFlow-orange.svg">
  <img src="https://img.shields.io/badge/-sklearn-orange.svg">
  <img src="https://img.shields.io/badge/-Numpy-blue.svg">
  <img src="https://img.shields.io/badge/-Pandas-blue.svg">
  <img src="https://img.shields.io/badge/-Matplotlib-blue.svg">
  <img src="https://img.shields.io/badge/-Seaborn-lightblue.svg">
  <img src="https://img.shields.io/badge/-Jupyter-lightgrey.svg">
</div>

## Introduction
> [!IMPORTANT]  
> This project uses the [NSL-KDD](https://ieee-dataport.org/documents/nsl-kdd-0) dataset to train models, and the table below outlines the general research methodology and approach.  
> If interested, you can view the following links:  
> 1. [A Deeper Dive into the NSL-KDD Data Set](https://towardsdatascience.com/a-deeper-dive-into-the-nsl-kdd-data-set-15c753364657)  
> 2. [Network Intrusion Detection using Deep Learning](https://medium.com/geekculture/network-intrusion-detection-using-deep-learning-bcc91e9b999d)  
> 3. [Network Intrusion Detection: An Analytical Assessment Using Deep Learning and State-of-the-Art Machine Learning Models](https://link.springer.com/article/10.1007/s44196-021-00047-4)

| **Research Phase**     | **Description**                                                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Background and Challenges | Faced with cybersecurity challenges, cyber threat cognitive systems can quickly identify threats and provide insights for defense strategies.      |
| Threat Detection Methods  | - `Signature-based`: High accuracy but limited against `zero-day attacks`.<br>- `Anomaly-based`: Effectively complements signature-based methods.      |
| Dataset Issues           | - `NSL-KDD` dataset is commonly used but lacks thorough exploratory analysis.<br>- Mismatched category distribution between training and test sets with insufficient `R2L` and `U2R` samples. |
| Methodological Solutions | - Merge and re-partition datasets to ensure comprehensiveness and representativeness.<br>- Encode data using `One-Hot` and `Label-Encoding` after re-partitioning.<br>- Standardize data using `Z-Score`.<br>- Apply feature extraction (`Mutual Information`, `Pearson Correlation`) or feature selection (`LDA`, `PCA`). |
| Model Training and Evaluation | - Conduct initial training using `SVM`, `RF`, and `Bi-LSTM` to identify the best performing model.<br>- Enhance training set using data augmentation techniques `SMOTE` and `ADASYN`.<br>- Retrain the enhanced dataset through `SVM`, `RF`, and `Bi-LSTM` to develop the final model.<br>- Evaluate using multiple metrics: `Accuracy`, `Precision`, `Recall`, `F1 Score`, `MCC`, and `FAR`.          |
| Cognitive System Development | Integrate models into a system developed with `PyQt5` with crawler-based intelligence gathering and a user-friendly interface.                                |

## Methodology
> [!NOTE]
> 1. Includes two core components: `Threat detection (First Picture Below）`and `Intelligence collection (Second Picture Below)`
> 2. For the `Threat detection module`, the system utilizes `SVM`, `RF`, and `Bi-LSTM` to achieve efficient threat identification.
> 3. The `Intelligence collection module` mainly gathers threat-related data from various `security intelligence center websites` through web crawling technology.
<div align="left">
  <img src="https://github.com/user-attachments/assets/daf76387-0fad-417a-a36c-9256460a2cbb" height="257">
  <img src="https://github.com/user-attachments/assets/e525911c-0282-40cb-b1e0-f94c7374a4ad" width="500">
</div>

## CTCS (Cyber Threat Cognitive System)
> [!NOTE]
> 1. [This software is developed using `PyQT5`. You can download the code, set up the environment and the corresponding packages, and run `MainWindow.py` to start the application.](https://github.com/DarrylXzq/CTCS/tree/master/pyqt_code)
> 2. [Users can download the corresponding models as needed and deploy them into the system (Model Management).](https://github.com/DarrylXzq/CTCS/tree/master/model)
> 3. Users can upload the corresponding `CSV` files that need to be detected for analysis.
> 4. The system supports multithreading, enabling file detection while simultaneously utilizing the `Intelligence Collection Module` to obtain the latest cybersecurity intelligence.
> 5. Below is the actual `software interface` and `a demo during operation`.

> [!WARNING]
> 1. Models trained using Bi-LSTM require a `TensorFlow 2.0` or above framework to run (GPU is needed).
> 2. Uploaded `CSV` files should conform to the `NSL-KDD dataset specifications`, otherwise a format error will be prompted [(see this table for specific ranges)](https://docs.google.com/spreadsheets/d/1oAx320Vo9Z6HrBrL6BcfLH6sh2zIk9EKCv2OlaMGmwY/edit?gid=0#gid=0).

<div align="left">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/home_page.png" width="250">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/model_management.png" width="250">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/model_detection.png" width="250">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/intelligence_%20system.png" width="250">
  <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/detection_report.png" height="200">
  <a href="https://github.com/DarrylXzq/CTCS_Code/blob/master/interface_figure/video/run_video.mp4">
    <img src="https://github.com/DarrylXzq/CTCS_Code/blob/master/pyqt_code/CTCS/resource/figure/start.png" alt="Watch the video" height="170">
  </a>
</div>

##  Usage Restrictions
> [!WARNING]
> 1. This project and its code may `not` be used for any form of `commercial sales or services`.
> 2. The project must `not` be used as or embedded in any `commercial product`.


## 😄 Acknowledgements

 - Thanks to the family, supervisors, and friends for their help.👋👋👋
 - [github-readme-stats](https://github.com/anuraghazra/github-readme-stats/blob/master/readme.md)
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## 👋 Feedback

If you have any feedback, please reach out to us at `xiangzq.darryl@gmail.com`

