# F01-I3: rPPG Metric Audit

## Project Overview

This project investigates how the choice of evaluation metric affects the ranking of remote photoplethysmography (rPPG) methods.

Remote photoplethysmography (rPPG) estimates physiological signals such as heart rate from ordinary camera video by analyzing subtle changes in facial skin color caused by blood flow.

The goal of this project is not to develop a new rPPG method. Instead, we will evaluate established rPPG methods using the same experimental protocol and investigate whether different evaluation metrics produce different conclusions about which method performs best.

---

## Core Question

> **Does the metric you use change which method wins?**

Different metrics measure different properties of an estimated physiological signal. A method that performs well according to one metric may not necessarily perform equally well according to another.

This project will systematically compare the rankings produced by different metrics.

---

## Methods

We will evaluate the following five established rPPG methods:

1. **GREEN**
   - A classical method based primarily on the green color channel.

2. **CHROM**
   - A classical chrominance-based method that uses color information to reduce the effect of motion and illumination changes.

3. **POS**
   - A chrominance-based method that uses a projection approach to extract the pulse signal from facial video.

4. **DeepPhys**
   - A deep-learning-based rPPG method that learns spatial and temporal physiological patterns from video.

5. **TS-CAN**
   - A temporal-shift convolutional attention network designed to efficiently capture temporal information for rPPG estimation.

---

## Evaluation Metrics

Each method will be evaluated using four metrics:

### 1. MAE — Mean Absolute Error

Measures the average absolute difference between the estimated heart rate and the reference heart rate.

Lower MAE is better.

### 2. RMSE — Root Mean Squared Error

Measures the square root of the average squared error between estimated and reference heart rates.

Lower RMSE is better.

### 3. Pearson r

Measures the correlation between the estimated and reference signals.

Higher Pearson correlation is better.

### 4. Waveform SNR — Signal-to-Noise Ratio

Measures the quality of the extracted pulse waveform relative to noise.

Higher SNR is better.

---

## Datasets

The analysis will use two established rPPG datasets:

- **PURE**
- **UBFC-rPPG**

These datasets provide facial video recordings together with reference physiological measurements that can be used to evaluate rPPG predictions.

---

## Experimental Question

The central investigation is whether the five methods receive consistent rankings across all four metrics.

For example:

- Does the method with the lowest MAE also have the best RMSE?
- Does the method with the highest Pearson correlation also have the best waveform SNR?
- Can a method rank highly under one metric but poorly under another?
- Does the choice of metric change the overall conclusion about which rPPG method performs best?

The experiment will keep the evaluation protocol and predictions fixed so that differences in rankings can be attributed to the evaluation metrics rather than changes in the underlying predictions or processing pipeline.
