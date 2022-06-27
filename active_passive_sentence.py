import spacy
from spacy.matcher import Matcher

PRONOUNS = {'her ':'she ', 'him ':'he ', 'whom ':'who ', 'me ': 'I ', 'us ':'we ', 'them ':'they '}
LIST_PRONOUNS = {'who'}
SUBJECTS = ['nsubj', 'nsubjpass']
SUBJECTS_ACTIVE = ['nsubj']
SUBJECTS_PASSIVE = ['nsubjpass']

class ActivePassiveSentence:
    def __init__(self, sentence):
        self.nlp = spacy.load('en_core_web_sm')
        self.doc = self.nlp(sentence)
        self.sentence = sentence
        self.svo = []
        
    def get_active_passive_sentence(self):
        matcher = Matcher(self.nlp.vocab)
        passive_rule = [{'DEP': 'nsubjpass'}, {'DEP': 'aux', 'OP': '*'}, {'DEP': 'auxpass'}, {'TAG': 'VBN'}]
        matcher.add('Passive', None, passive_rule)
        matches = matcher(self.doc)
        if matches:
            return "Passive"
        else:
            return "Active"
    
    def convert_active_to_passive_sentence(self):
        s = list(self.doc)
        tmp,temp,sub = "","",-1
        for i in self.doc:
            if i.pos_ == 'VERB':
                s[i.i] = i
            elif i.dep_ == 'nsubj':
                sub = i.i
                temp = i
            elif i.dep_ == 'dobj':
                tmp = i.text.capitalize()
                s[i.i] = temp
                s.insert(i.i,"by")
        s[sub] = tmp
        return ' '.join(str(e) for e in s)
    
    def get_multiple_subject_from_sentence(self):
        # sentence = "John and Jenny were accused of crimes by David"
        sent = self.nlp(self.sentence)
        result = []
        subj = None
        for word in sent:
            if 'subj' in word.dep_:
                subj = word
                result.append(word)
            elif word.dep_ == 'conj' and word.head == subj:
                result.append(word)
        return result
    
    def get_multiple_verb_from_sentence(self):
        # sentence = "the supervisor must approve or reject the request"
        sent = self.nlp(self.sentence)
        result = []
        subj = None
        for word in sent:
            if 'ROOT' in word.dep_:
                subj = word
                result.append(word)
            elif word.dep_ == 'conj' and word.head == subj:
                result.append(word)
        return result
    
    # det + compound + compound + nsubj <- [ROOT]
    def _get_subject(self, token, index_counter):
        recipient_index = None
        if token.dep_ in SUBJECTS:
            recipient_index = index_counter
            recipient = token.lower_
            article_list = [t.text for t in token.lefts]
            try:
                compound_article = ' '.join(article_list).lower()
            except:
                compound_article = ''
            return recipient_index, recipient, compound_article
    
    def _get_verb(self, token, index_counter):
        main_verb_index = None
        if token.dep_ == 'ROOT':
            main_verb_index == index_counter
            main_verb = token.text
            base_form_of_main_verb = token.lemma_    
            return main_verb_index, base_form_of_main_verb, main_verb
    
    def _get_agent(self, token, index_counter):
        agent_index = None
        append = False
        agent = ''
        if token.dep_ == 'agent':
            agent_index = index_counter
            agent_children_list = [t.text for t in token.rights]
            agent_children_right = ' '.join(agent_children_list)
            agent = token.text + ' ' + agent_children_right
            agent_children_left = [t.text for t in token.lefts]
            append = True
        return agent_index, agent, agent_children_right, agent_children_left, append  
    
    def _get_is_punct(self, token, agent):
        sentence_remainder = []
        if agent and not token.is_punct:
            sentence_remainder.append(token)
        return sentence_remainder
    
    def _is_punct(self, token):
        if token.is_punct:
            punct = token.text
        return punct
    
    def _get_agent_from_pobj(self, token):
        append = False
        if token.dep_ == 'pobj':
            append = False
            if not agent:
                agent = token.text
        return append, agent
    
    def _get_agent_from_pronoun_list(self):
        for key, value in PRONOUNS.items():
            if key in agent.lower() + ' ':
                agent = value.strip()
        return agent
        
    def _get_modal_verb(self, token):
        inflection = ''
        if token.text in ['may', 'must', 'might', 'could', 'will']:
            inflection = ' ' + token.text + ' '
        index_counter += 1
        return index_counter, inflection

    def _get_punct(self, punct, sent):
        start_word = ''
        if punct in ['?']:
            for token in sent:
                if token.text in ['Can', 'May']:
                    start_word = token.text
                    break
        return start_word
    
    def _get_agent_article(self, sentence_remainder):
        index = 0 
        for t in sentence_remainder:
            if t.pos_ in ['DET'] and index >= 2:
                agent_article = t.text
                index += 1
        return agent_article
    
    def svo_pattern(self, subject, verb, dobj):
        #Active : nsubj + [ROOT, verb, advcl, relcl] + dobj
        #Passive : nsubjpass + [ROOT] -> convert to -> ROOT + nsubj
        self.svo.append('{} {} {}'.format(subject, verb, dobj))

    def convert_passive_to_active_sentence(self):
        for sent in self.doc.sents:
            sent_list = []
            for token in sent:
                sent_list.append(token)
            
            subject = ""
            compound_article = ""
            main_verb_index = None
            main_verb = ""
            main_object_index = None
            main_object = ""
            agent = ''
            sentence_remainder = []
            index_counter = 0
            svo_list = []

            for token in sent_list:                
                #SUBJECT
                if token.dep_ in ["nsubj", "nsubjpass"]:
                    subject = token.text
                    article_list = [t.text for t in token.lefts]
                    try:
                        compound_article = ' '.join(article_list).lower() + ' ' + subject
                    except:
                        compound_article = ' ' + subject

                #VERB
                if token.dep_ in ['ROOT','advcl','relcl']:
                    main_verb_index == index_counter
                    main_verb = token.text
                
                elif token.dep_ in ['dobj']:
                    main_object_index == index_counter
                    main_object = token.text
                
                #AGENT
                elif token.dep_ == 'agent':
                    agent_children_list = [t.text for t in token.rights]
                    agent_children_right = ' '.join(agent_children_list)
                    agent = token.text + ' ' + agent_children_right
                    print("agent", agent)

                #PUNCT
                elif agent and not token.is_punct:
                    sentence_remainder.append(token)
                
                elif token.is_punct:
                    punct = token.text
                    print("punct", punct)
                
                #POBJ
                elif token.dep_ == 'pobj':
                    if not agent:
                        agent = token.text
                        print("agent_pobj", agent)
                
                #CONVERT who => POBJ
                elif token.text in LIST_PRONOUNS:
                    print("agent.lower()::", agent.lower())

                svo_list.append((compound_article, main_verb, main_object, agent))


    def convert_passive_to_active_sentence(self):
        for sent in self.doc.sents:
            try:
                sent_list = []
                for token in sent:
                    sent_list.append(token)

                subject = ""
                compound_article = ""
                main_verb_index = None
                agent_index = None
                recipient_index = None
                agent = ''
                inflection = ''
                agent_article = ''
                start_word = ''
                sentence_remainder = []
                index_counter = 0

                for token in sent_list:
                    if token.dep_ in ["nsubj", "nsubjpass"]:
                        subject = token.text
                        recipient_index = index_counter
                        recipient = token.lower_
                        article_list = [t.text for t in token.lefts]
                        try:
                            compound_article = ' '.join(article_list).lower() + ' ' + subject
                        except:
                            compound_article = ' ' + subject

                    #VERB
                    elif token.dep_ in ['ROOT']:
                        main_verb_index == index_counter
                        main_verb = token.text
                                        
                    #AGENT
                    elif token.dep_ == 'agent':
                        agent_index = index_counter
                        agent_children_list = [t.text for t in token.rights]
                        agent_children_right = ' '.join(agent_children_list)
                        agent = token.text + ' ' + agent_children_right

                    #PUNCT
                    elif agent and not token.is_punct:
                        sentence_remainder.append(token)
                    
                    elif token.is_punct:
                        punct = token.text
                    
                    #POBJ
                    elif token.dep_ == 'pobj':
                        if not agent:
                            agent = token.text
                    
                    #MODAL VERB
                    elif token.text in ['may', 'must', 'might', 'could', 'will']:
                        inflection = ' ' + token.text + ' '
                    index_counter += 1

                #QUESTION
                if punct in ['?']:
                    for token in sent:
                        if token.text in ['Can', 'May']:
                            start_word = token.text
                            break
                
                #PRONOUN
                for key, value in PRONOUNS.items():
                    if key in agent.lower() + ' ':
                        agent = value.strip()

                index = 0 
                for t in sentence_remainder:
                    if t.pos_ in ['DET'] and index >= 2:
                        agent_article = t.text
                        index += 1

                #RESULT
                if recipient_index < agent_index:
                    return '{} {} {} {}{} {} {}{}'.format(
                            start_word, agent_article, agent, inflection, main_verb, compound_article, recipient, punct).replace('by ', '')

            except:
                return sent