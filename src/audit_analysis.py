import os
import pickle
import numpy as np
import pandas as pd


AUDIT_DIR = "data/frozen_predictions"

METHOD_FILES = {
    "CHROM": "CHROM_audit.pkl",
    "GREEN": "GREEN_audit.pkl",
    "POS": "POS_audit.pkl",
}


def load_audit_data(filename):
    path = os.path.join(AUDIT_DIR, filename)

    with open(path, "rb") as f:
        data = pickle.load(f)

    return data


def calculate_audit_metrics(data):
    hr_pred = []
    hr_gt = []
    snr = []

    for item in data:
        if item.get("hr_pred") is not None and item.get("hr_gt") is not None:
            hr_pred.append(float(item["hr_pred"]))
            hr_gt.append(float(item["hr_gt"]))

        if item.get("snr") is not None:
            snr.append(float(item["snr"]))

    hr_pred = np.array(hr_pred, dtype=float)
    hr_gt = np.array(hr_gt, dtype=float)
    snr = np.array(snr, dtype=float)

    valid_hr = np.isfinite(hr_pred) & np.isfinite(hr_gt)

    hr_pred = hr_pred[valid_hr]
    hr_gt = hr_gt[valid_hr]

    mae = np.mean(np.abs(hr_pred - hr_gt))

    rmse = np.sqrt(
        np.mean((hr_pred - hr_gt) ** 2)
    )

    if len(hr_pred) > 1 and np.std(hr_pred) > 0 and np.std(hr_gt) > 0:
        pearson = np.corrcoef(hr_pred, hr_gt)[0, 1]
    else:
        pearson = np.nan

    snr = snr[np.isfinite(snr)]

    if len(snr) > 0:
        mean_snr = np.mean(snr)
    else:
        mean_snr = np.nan

    return {
        "MAE": mae,
        "RMSE": rmse,
        "Pearson r": pearson,
        "SNR (dB)": mean_snr,
        "Samples": len(hr_pred)
    }


def main():

    results = []

    print("\n==============================")
    print("       rPPG AUDIT ANALYSIS")
    print("==============================\n")

    for method, filename in METHOD_FILES.items():

        print(f"Loading {method}...")
        data = load_audit_data(filename)

        metrics = calculate_audit_metrics(data)

        results.append({
            "Method": method,
            **metrics
        })

    df = pd.DataFrame(results)

    print("\n==============================")
    print("        METRIC RESULTS")
    print("==============================\n")

    print(
        df.to_string(
            index=False,
            float_format=lambda x: f"{x:.4f}"
        )
    )

    print("\n==============================")
    print("          RANKINGS")
    print("==============================\n")

    mae_rank = df.sort_values("MAE")["Method"].tolist()
    rmse_rank = df.sort_values("RMSE")["Method"].tolist()
    pearson_rank = df.sort_values(
        "Pearson r",
        ascending=False
    )["Method"].tolist()
    snr_rank = df.sort_values(
        "SNR (dB)",
        ascending=False
    )["Method"].tolist()

    print("MAE      (lower is better): ", " > ".join(mae_rank))
    print("RMSE     (lower is better): ", " > ".join(rmse_rank))
    print("Pearson r (higher is better):", " > ".join(pearson_rank))
    print("SNR      (higher is better): ", " > ".join(snr_rank))

    print("\n==============================")
    print("          RANK TABLE")
    print("==============================\n")

    ranking = pd.DataFrame({
        "Method": df["Method"],
        "MAE Rank": df["MAE"].rank(
            method="min",
            ascending=True
        ).astype(int),
        "RMSE Rank": df["RMSE"].rank(
            method="min",
            ascending=True
        ).astype(int),
        "Pearson Rank": df["Pearson r"].rank(
            method="min",
            ascending=False
        ).astype(int),
        "SNR Rank": df["SNR (dB)"].rank(
            method="min",
            ascending=False
        ).astype(int)
    })

    print(ranking.to_string(index=False))


if __name__ == "__main__":
    main()