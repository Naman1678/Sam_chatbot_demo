from datasets import load_dataset
import json
import os


def download_and_save_annotations():
    print("Downloading MSR-VTT dataset...")

    dataset = load_dataset("friedrichor/MSR-VTT", "test_1k")

    data_list = []

    for item in dataset["test"]:
        video_id = item["video_id"]
        caption = item["caption"]

        data_list.append({
            "video_id": video_id,
            "caption": caption
        })

    os.makedirs("data", exist_ok=True)

    with open("data/msrvtt_annotations.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4)

    print("Saved annotations to data/msrvtt_annotations.json")


if __name__ == "__main__":
    download_and_save_annotations()