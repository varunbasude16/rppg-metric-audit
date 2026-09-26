# Discussion

## GREEN Rank Swap

The audit shows that GREEN performs differently depending on the metric being considered. While GREEN performs relatively well in terms of Pearson correlation, indicating that it tracks the trend of the reference heart-rate signal reasonably well, it performs poorly in terms of absolute error (MAE).

Compared with POS and CHROM, this demonstrates a clear rank swap: GREEN is better at tracking the trend of the signal than at accurately estimating its absolute value. Therefore, a method can achieve a relatively strong correlation while still producing large absolute errors.

## Windowing Confound

There is an important difference in the number of evaluated samples between the unsupervised and neural methods. CHROM, GREEN, and POS were evaluated using 439 samples, whereas DeepPhys and TS-CAN were evaluated using 41 samples.

This difference comes from the evaluation setup: the unsupervised methods were evaluated over many short windows, while the neural methods were evaluated using full videos. Consequently, the two groups are not being evaluated over exactly the same number or type of samples.

This is an important confound when comparing rPPG methods. Differences in windowing and evaluation protocol can affect the resulting metrics and rankings, and inconsistent evaluation protocols are a common issue in rPPG reporting.

## Conclusion

The central conclusion of this audit is that **yes, the metric chosen can change which method appears to perform best**.

Metrics measure different aspects of performance. Pearson correlation emphasizes how well the predicted signal follows the trend of the reference signal, while MAE measures the magnitude of the absolute error. As demonstrated by the GREEN rank swap, a method can perform relatively well on correlation while performing poorly on absolute error.

Therefore, reporting only a single metric, such as Pearson correlation, can hide important weaknesses in other aspects of performance, such as MAE. A more reliable comparison should report multiple complementary metrics and should also use consistent evaluation protocols across methods.