#%%
import json

# Paths to the JSON files
train_images_path = "JSONdata/TRAIN_images.json"
train_objects_path = "JSONdata/TRAIN_objects.json"
test_images_path = "JSONdata/TEST_images.json"
test_objects_path = "JSONdata/TEST_objects.json"

# Function to load and inspect JSON files
def inspect_json(file_path, num_samples=5):
    with open(file_path, "r") as f:
        data = json.load(f)
    print(f"Inspecting {file_path}:")
    if isinstance(data, list):
        print(f"Total Entries: {len(data)}")
        print("Sample Entries:", data[:num_samples])
    elif isinstance(data, dict):
        print(f"Keys: {list(data.keys())}")
        print("Sample Entries:", {k: data[k] for k in list(data.keys())[:num_samples]})
    print("\n")

# Inspect each file
inspect_json(train_images_path)
inspect_json(train_objects_path)
inspect_json(test_images_path)
inspect_json(test_objects_path)

# %%
