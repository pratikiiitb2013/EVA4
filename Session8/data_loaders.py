from imports_eva import *
from params import *

'''
try:
	with open("params.json") as f:
		params = json.load(f)
except IOError as e:
	raise e
'''


def train_test_loaders():
  transform_names =  [k for k,v in params["transforms"].items() if v is True]
  train_transform_list = []
  for t in transform_names:
    train_transform_list.append(getattr(transforms, t)(**params['transform_values'][t]))
    
  train_transform_list.append(transforms.ToTensor())
  train_transform_list.append(transforms.Normalize(**params[params["dataset"] + '_normalize_values']))
  train_transform = transforms.Compose(train_transform_list)
  trainset = getattr(datasets, params["dataset"])(root='./data', train=True, 
                                         download=True, transform=train_transform)
  test_transform = transforms.Compose([transforms.ToTensor(), 
                                      transforms.Normalize(**params[params["dataset"] + '_normalize_values'])])
  testset = getattr(datasets, params["dataset"])(root='./data', train=False,
                                          download=True, transform=test_transform)

  trainloader = torch.utils.data.DataLoader(trainset, batch_size=params["batch_size"],
                                            shuffle=True, num_workers=params["n_workers"])
  testloader = torch.utils.data.DataLoader(testset, batch_size=params["batch_size"],
                                            shuffle=False, num_workers=params["n_workers"])
  return trainloader, testloader