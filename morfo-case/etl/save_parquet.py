#import numpy as np
#import os
#import pandas as pd
#from analyze_batches import analyze_batch
#
#def main():
#    results = []
#    for i in range(1, 6):
#        path = f"data/batch_{i}"
#        res = analyze_batch(path)
#        results.append({
#            "batch_id": f"batch_{i}",
#            "white_avg": res["white"]["avg"],
#            "white_std": res["white"]["std"],
#            "white_min": res["white"]["min"],
#            "white_max": res["white"]["max"],
#            "black_avg": res["black"]["avg"],
#            "black_std": res["black"]["std"],
#            "black_min": res["black"]["min"],
#            "black_max": res["black"]["max"],
#        })
#
#    df = pd.DataFrame(results)
#    df.to_parquet("data/batch_summary.parquet", index=False)
#    print("Parquet file saved at: data/batch_summary.parquet")
#
#
#if __name__ == "__main__":
#    main()

import numpy as np
import os
import pandas as pd
import boto3
from etl.analyze_batches import analyze_batch

def upload_to_s3(local_path, bucket, key):
    s3 = boto3.client("s3")
    s3.upload_file(local_path, bucket, key)
    print(f"✅ Uploaded to s3://{bucket}/{key}")

def main():
    results = []
    for i in range(1, 6):
        path = f"data/batch_{i}"
        res = analyze_batch(path)
        results.append({
            "batch_id": f"batch_{i}",
            "white_avg": res["white"]["avg"],
            "white_std": res["white"]["std"],
            "white_min": res["white"]["min"],
            "white_max": res["white"]["max"],
            "black_avg": res["black"]["avg"],
            "black_std": res["black"]["std"],
            "black_min": res["black"]["min"],
            "black_max": res["black"]["max"],
        })

    df = pd.DataFrame(results)
    local_file = "data/batch_summary.parquet"
    df.to_parquet(local_file, index=False)
    print("✅ batch_summary.parquet saved.")

    # Upload to S3 (question 8)
    upload_to_s3(local_file, "raw", "test/test.parquet")

if __name__ == "__main__":
    main()
