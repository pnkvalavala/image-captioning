from torch.utils.data import DataLoader
from coco_dataset import CocoDataset

def get_loader(transform):
    dataset = CocoDataset("coco_dataset/train2017", "coco_dataset/annotations/captions_train2017.json", transform)
    data_loader = DataLoader(dataset)
    return data_loader