from model.model import CustomPatchTSTClassifier
import torch

# Hyper Params
context_length = 200
num_input_channels = 3
num_classes_per_category = 3
num_categories = 4
patch_length = 8
device= 'cuda'

custom_model = CustomPatchTSTClassifier(num_input_channels=num_input_channels,
                                        context_length=context_length,
                                        patch_length=patch_length,
                                        num_classes_per_category=num_classes_per_category,
                                        num_categories=num_categories,
                                        use_cls_token=True)
custom_model = custom_model.to(device)

# (batch_size, context_length, num_input_channels)
past_values = torch.randn(32, context_length, num_input_channels).to(device)

output = custom_model(past_values)
probabilities = torch.softmax(output, dim=-1)
