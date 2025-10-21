from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertModel, BertLMPredictionHead

from utils import Similarity, Pooler
from module import jt_module




class JobMatchingMultiTaskModel(BertPreTrainedModel):
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config, *args, **kwargs):
        super().__init__(config)
        self.model_args = kwargs["model_args"]
        self.data_args = kwargs["data_args"]
        self.pooler_type = kwargs["model_args"].pooler_type
        self.pooler = Pooler(kwargs["model_args"].pooler_type)

        self.model = BertModel(config, add_pooling_layer=False)
        self.cosine_similarity = Similarity(temp=self.model_args.temp)
        self.loss_fun = nn.CrossEntropyLoss()

        self.init_weights()


    def forward(self,
        input_ids=None,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
        sent_emb=False,
        mlm_input_ids=None,
        mlm_labels=None,
    ):
    
        loss = jt_module(self, self.model,
                input_ids=input_ids,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids,
                position_ids=position_ids,
                head_mask=head_mask,
                inputs_embeds=inputs_embeds,
                labels=labels,
                output_attentions=output_attentions,
                output_hidden_states=output_hidden_states,
                return_dict=return_dict,
                mlm_input_ids=mlm_input_ids,
                mlm_labels=mlm_labels
            )            

        return loss