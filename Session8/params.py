params  = {
  "model": "resnet18",
  "dataset": "CIFAR10",
  "CIFAR10_normalize_values": {"mean" : (0.5, 0.5, 0.5), "std" : (0.5, 0.5, 0.5)},
  "MNIST_normalize_values": {"mean" : (0.1307,), "std" : (0.3081,)},
  "batch_size" : 128,
  "transforms" : {
					"RandomHorizontalFlip" : True, 
					"RandomRotation" : True,
					"ColorJitter" : True
				},
  "transform_values" : {
            "RandomHorizontalFlip" : {"p" :0.5},
						"RandomRotation" : {"degrees" : 5},
						"ColorJitter" : {"hue" : 0.05, "saturation" : 0.05}
						},
  "n_workers" : 2,
  "dropout" : 0.1
}