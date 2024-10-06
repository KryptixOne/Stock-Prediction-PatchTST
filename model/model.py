import torch
import torch.nn as nn
from transformers import PatchTSTConfig, PatchTSTModel


class CustomPatchTSTClassifier(nn.Module):
    def __init__(self, num_input_channels, context_length, patch_length,
                 num_classes_per_category=3, num_categories=4, use_cls_token=True):
        super().__init__()

        # Configure PatchTSTModel
        self.config = PatchTSTConfig(
            num_input_channels=num_input_channels,
            context_length=context_length,
            patch_length=patch_length,
            use_patch_pe=True,        # Ensure positional encoding is used
            use_vars_per_channel=True # Depending on your data
        )
        self.base_model = PatchTSTModel(self.config)

        # Retrieve hidden size from the base model configuration
        hidden_size = self.config.hidden_size

        # Single classification head for all categories
        self.fc = nn.Linear(hidden_size, num_categories * num_classes_per_category)

        # Option to use CLS token or mean pooling
        self.use_cls_token = use_cls_token

        # Store other parameters
        self.num_classes_per_category = num_classes_per_category
        self.num_categories = num_categories

    def forward(self, past_values):
        # Get hidden states from PatchTSTModel
        outputs = self.base_model(past_values=past_values)
        hidden_states = outputs.last_hidden_state  # Shape: (batch_size, seq_len, hidden_size)
        print(f'hidden_state from patchtst base model is {hidden_states.shape}')

        # Use CLS token state or mean pooling based on the hyperparameter
        if self.use_cls_token:
            output_state = hidden_states[:,:,0, :]  # Assuming CLS token is at position 0
            output_state = output_state.mean(dim=1)
        else:
            output_state = hidden_states.mean(dim=2).mean(dim=1)

        print(f'pre-head shape {output_state.shape}')
        # Generate logits for all categories
        logits = self.fc(output_state)  # Shape: (batch_size, num_categories * num_classes_per_category)
        print(f'post_head shape {output_state.shape}')
        # Reshape logits to (batch_size, num_categories, num_classes_per_category)
        logits = logits.view(-1, self.num_categories, self.num_classes_per_category)

        return logits  # Returns tensor of logits
