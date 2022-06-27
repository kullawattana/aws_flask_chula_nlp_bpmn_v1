## Step 1 Merge Phrase

```python
doc = self.nlp(sentence)
doc = self.merge_phrases()
doc = self.merge_phrases()
```

## Step 2 Get Subject, Verb, Object

```python
s = GetSubject()
v = GetVerb() 
o = GetObject()
```

## Step 3

```python
#1
is_pas = self.is_passive(doc)           
verbs = v.main_find_verbs(doc)
#2
subs, verbNegated = s.main_get_all_subs(verb)               
isConjVerb, conjV = v.right_of_verb_is_conj_verb(verb)      
#3
v2, objs = o.main_get_all_objs(conjV, is_pas)
verb, objs = o.main_get_all_objs(verb, is_pas) 
#4
signal_word, _event_label = self.get_signal_word_show_gateway(is_show_gateway, verb)
```

# ====================================
# Group 1
# ====================================
## Sentence 1
Ex: The Vacation Request Process starts when an employee of the organization submits a vacation request.

## Start
1. Verb
verbs => [starts, submits]
Ex: The Vacation Request Process [starts] when an employee of the organization [submits] a vacation request.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (more than 1 to extend)
Subject => [The Vacation Request Process]
Subject => [an employee]
Ex: {The Vacation Request Process} [starts] when {an employee} of the organization [submits] a vacation request.
4. isConjVerb 
starts => False
submits => False
5. Object
Ex: {The Vacation Request Process} [starts] when {an employee} of the organization [submits] <a vacation request>.
verb, objs => starts, []
verb, objs => submits, [a vacation request]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. check V,O => ให้ได้เป็น active sentence 
ถ้าไม่มี object จะไม่นำมาใช้เป็นชื่อกิจกรรม แต่ถ้าเป็นคำว่า starts ถือว่าเป็นคำที่บอกว่าคือ เริ่มต้นกิจกรรม
- {The Vacation Request Process}, starts, [] 
### Check Verbs => starts
### convert to active => {The Vacation Request Process}, starts, [] 
### VO: starts, [] 
### Subject: {The Vacation Request Process}
- {an employee}, submits, [a vacation request]
### Check Verbs => submits
### convert to active => {an employee}, submits, [a vacation request]
### VO: submits, [a vacation request] 
### Subject: {an employee}

# ====================================
## Sentence 2
Ex: Once the requirement is registered, the request is received by the immediate supervisor;

## Start
1. Verb
verbs => [registered, received]
Ex: Once the requirement is [registered], the request is [received] by the immediate supervisor;
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (more than 1 to extend)
Subject => [the requirement]
Subject => [the request]
Ex: Once {the requirement} is [registered], {the request} is [received] by the immediate supervisor;
4. isConjVerb 
registered => False
received => False
5. Object (Check Passive "the request is received by the immediate supervisor" and convert to Active)
Ex: Once {the requirement} is [registered], {the request} is [received] by the <immediate supervisor>;
verb, objs => registered, []
verb, objs => received, [the immediate supervisor]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. check V,O => ถ้าเป็น passive sentence ให้ทำการ convert เป็น active sentence แล้วให้ดูว่ามี V,O ครบ ถือว่าเป็นชื่อกิจกรรม
- {the requirement}, registered, []
### Check Verbs => registered
### convert to active => [], register, {the requirement}
### VO: register, {the requirement} 
### Subject: []
- {the request}, received, [the immediate supervisor] 
### Check Verbs => received
### convert to active => [the immediate supervisor], receive, {the request}  
### VO: receive, {the request}  
### Subject: [the immediate supervisor]

# ====================================
## Sentence 3
Ex: the supervisor must approve or reject the request.

## Start
1. Verb
verbs => [approve, reject]
Ex: the supervisor must [approve] or [reject] the request.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (more than 1 to extend)
Subject => [the supervisor]
Subject => []
Ex: {the supervisor} must [approve] or [reject] the request.
4. isConjVerb 
approve => True, 
reject => False
5. Object
Ex: {the supervisor} must [approve] or [reject] <the request>.
verb, objs => [], []
verb, objs => reject, [the request]
6. Label
signal_word, _event_label => _, _
signal_word, _event_label => _, VO_

## Result SVO
1. check V,O => ถ้าเป็น passive sentence ให้ทำการ convert เป็น active sentence แล้วให้ดูว่ามี V,O ครบ ถือว่าเป็นชื่อกิจกรรม
- {the supervisor}, [], []
### Check Verbs => [] => No verb (Try to check again)
### convert to active => 
### VO:  
### Subject: 
- {the supervisor}, reject, [the request] 
### Check Verbs => reject
### convert to active => {the supervisor}, reject, [the request]  
### VO: reject, [the request]
### Subject: {the supervisor}

# ====================================
## Sentence 4
Ex: If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons.

## Start
1. Verb
verbs => [rejected, returned, review]
Ex: If the request is [rejected] the application is [returned] to the applicant/employee who can [review] the rejection reasons.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (more than 1 to extend)
Subject => [the request]
Subject => [the application]
Subject => [who]
Ex: If {the request} is [rejected] {the application} is [returned] to the applicant/employee {who} can [review] the rejection reasons.
4. isConjVerb 
rejected => False,
returned => False,
review => False
5. Object (Check Passive "the application is returned to the applicant/employee" and convert to Active)
Ex:  If {the request} is [rejected] {the application} is [returned] to <the applicant / employee> {who} can [review] <the rejection reasons>.
verb, objs => rejected, []
verb, objs => returned, [the applicant/employee]
verb, objs => review, [the rejection reasons]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. check V,O => ถ้าเป็น passive sentence ให้ทำการ convert เป็น active sentence แล้วให้ดูว่ามี V,O ครบ ถือว่าเป็นชื่อกิจกรรม
- {the request}, rejected, []
### Check Verbs => rejected 
### convert to active => [], reject, {the request}  
### VO: reject, [the request]
### Subject: []
- [the application], returned, <the applicant / employee>
### Check Verbs => rejected
### convert to active => <the applicant / employee>, return, [the application]  
### VO: return, {the request}
### Subject: <the applicant / employee>
- {who}, review, [the rejection reasons]
### Check Verbs => review
### Have subject => {who} 
### convert to active => {who} review, [the rejection reasons]  
### VO: review, [the rejection reasons]
### Subject: {who}

# ====================================
## Sentence 5
Ex: If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures.

## Start
1. Verb
verbs => [approved, generated, complete]
Ex: If the request is [approved] a notification is [generated] to the Human Resources representative, who must [complete] the respective administrative procedures.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (more than 1 to extend)
Subject => [the request]
Subject => [a notification]
Subject => [who]
Ex: If {the request} is [approved] {a notification} is [generated] to the Human Resources representative, {who} must [complete] the respective administrative procedures.
4. isConjVerb 
approved => False, 
generated => False, 
complete => False
5. Object (Check Passive "the application is returned to the applicant/employee" and convert to Active)
Ex: If {the request} is [approved] {a notification} is [generated] to <the Human Resources representative>, {who} must [complete] <the respective administrative procedures>.
verb, objs => approved, []
verb, objs => generated, [the Human Resources representative]
verb, objs => complete, [the respective administrative procedures]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. check V,O => ถ้าเป็น passive sentence ให้ทำการ convert เป็น active sentence แล้วให้ดูว่ามี V,O ครบ ถือว่าเป็นชื่อกิจกรรม
- {the request}, [approved], [] => convert to active => [approve], {the request}
### Check Verbs => approved
### convert to active => [], approve, {the request}
### VO: approve, {the request}
### Subject: []
- {a notification}, [generated], <the Human Resources representative> 
### Check Verbs => generated
### convert to active => <the Human Resources representative>, generate, {a notification}
### VO: generate, {a notification}
### Subject: <the Human Resources representative>
- {who} must [complete] <the respective administrative procedures>.
### Check Verbs => complete
### convert to active => {who}, [complete], <the respective administrative procedures>
### VO: [complete], <the respective administrative procedures> 
### Subject: {who}

# ===================================
# Group 2
# ===================================
## Sentence 1
Ex : The party sends a warrant possession request asking for a warrant to be released.

## Start
1. Verb
verbs => [sends, asking, released]
Ex: The party [sends] a warrant possession request [asking] for a warrant to be [released].
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject is 1 Extend)
Subject => [a warrant possession request]
Ex: {The party} [sends] a warrant possession request [asking] for a warrant to be [released].
4. isConjVerb 
sends => False, 
asking => False, 
released => False
5. Object
Ex: {The party} [sends] <a warrant possession request> [asking] for a warrant to be <[released]>.
verb, objs => sends, [a warrant possession request]
verb, objs => asking, [a warrant]
verb, objs => released, []
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. {The party} [sends] <a warrant possession request> [asking] a warrant to be [released].
### Check Verbs => sends
### convert to active => {The party} sends, [a warrant possession request]
### VO: sends, [a warrant possession request]
### Subject: {The party}

### Check Verbs => asking
### convert to active => {} ask, [a warrant]
### VO: ask, [a warrant]
### Subject: {}

### Check Verbs => released
### convert to active => [] release, {}
### VO: release {}
### Subject: {}

# ===================================
## Sentence 2
Ex : The Client Service Back Office as part of the Small Claims Registry Operations receives the request and retrieves the SCT file. 

## Start
1. Verb
verbs => [receives, retrieves]
Ex: The Client Service Back Office as part of the Small Claims Registry Operations [receives] the request and [retrieves] the SCT file. 
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [The Client Service Back Office]
Subject => []
Ex: {The Client Service Back Office} as part of the Small Claims Registry Operations [receives] the request and [retrieves] the SCT file. 
4. isConjVerb 
receives => False, 
retrieves => False
5. Object
Ex: {The Client Service Back Office} as part of the Small Claims Registry Operations [receives] <the request> and [retrieves] <the SCT file>. 
verb, objs => receives, [the request]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. {The Client Service Back Office} as part of the Small Claims Registry Operations [receives] <the request> and [retrieves] <the SCT file>.
### Check Verbs => receives
### convert to active => {The Client Service Back Office} receive, [the request]
### VO: receive, [the request]
### Subject: {The Client Service Back Office}

### Check Verbs => retrieves
### convert to active => {} retrieve, <the SCT file>
### VO: retrieve, <the SCT file>
### Subject: {}

# ===================================
## Sentence 3
Ex : Then, the SCT Warrant Possession is forwarded to Queensland Police.

## Start
1. Verb
verbs => [forwarded]
Ex: Then, the SCT Warrant Possession is [forwarded] to Queensland Police. 
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the SCT Warrant Possession]
Ex: Then, {the SCT Warrant Possession} is [forwarded] to Queensland Police. 
4. isConjVerb 
forwarded => False, 
5. Object
Ex: Then, {the SCT Warrant Possession} is [forwarded] to <Queensland Police>. 
verb, objs => forwarded, [Queensland Police]
6. Label
signal_word, _event_label => _, VO_

## Result SVO
1. Then, the SCT Warrant Possession is forwarded to Queensland Police.
### Check Verbs => forwarded
### convert to active => {Queensland Police}, forward, [the SCT Warrant Possession]
### VO: forward, [the SCT Warrant Possession]
### Subject: {Queensland Police}

# ===================================
## Sentence 4
Ex : The SCT physical file is stored by the Back Office awaiting a report to be sent by the Police.

## Start
1. Verb
verbs => [stored, awaiting, sent]
Ex: The SCT physical file is [stored] by the Back Office [awaiting] a report to be [sent] by the Police.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [ The SCT physical file]
Subject => []
Subject => [a report]
Ex: {The SCT physical file} is [stored] by the Back Office [awaiting] {a report} to be [sent] by the Police.
4. isConjVerb 
stored => False, 
awaiting => False,
sent => False, 
5. Object
Ex: {The SCT physical file} is [stored] by <the Back Office> [awaiting] <{a report}> to be [sent] by <the Police>.
verb, objs => stored, [the Back Office]
verb, objs => awaiting, [a report]
verb, objs => sent [the Police]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. {The SCT physical file} is [stored] by <the Back Office> [awaiting] <{a report}> to be [sent] by <the Police>.
### Check Verbs => stored
### {The SCT physical file}, [stored], <the Back Office>
### convert to active => <the Back Office>, store, {The SCT physical file}
### VO: store, {The SCT physical file}
### Subject: <the Back Office>

### Check Verbs => awaiting
### {}, [awaiting], [a report]
### convert to active => {}, [await], [a report]
### VO: [await], [a report]
### Subject: {}

# ===================================
## Sentence 5
Ex : When the report is received, the respective SCT file is retrieved.

## Start
1. Verb
verbs => [received, retrieved]
Ex: When the report is [received], the respective SCT file is [retrieved].
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the report]
Subject => [the respective SCT file]
Ex: When {the report} is [received], {the respective SCT file} is [retrieved].
4. isConjVerb 
received => False, 
retrieved => False,
5. Object
Ex: When {the report} is [received], {the respective SCT file} is [retrieved]
verb, objs => received, []
verb, objs => retrieved, []
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO
1. When {the report} is [received], {the respective SCT file} is [retrieved]
### Check Verbs => received
### {the report}, received, []
### convert to active => [], receive, {the report}
### VO: receive, {the report}
### Subject: <the Back Office>

### Check Verbs => retrieved
### {the respective SCT file}, retrieved, []
### convert to active => [], retrieve, {the respective SCT file}
### VO: receive, retrieve, {the respective SCT file}
### Subject: []

# ===================================
## Sentence 6
Ex : Then, Back Office attaches the new SCT document, and stores the expanded SCT physical file.

## Start
1. Verb
verbs => [attaches]
Ex: Then, Back Office [attaches] the new SCT document, and stores the expanded SCT physical file.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [Back Office]
Ex: Then, {Back Office} [attaches] the new SCT document, and stores the expanded SCT physical file.
4. isConjVerb 
attaches => False, 
5. Object
Ex: Then, {Back Office} [attaches] <the new SCT document>, and stores the expanded SCT physical file.
verb, objs => attaches, [the new SCT document, stores]
6. Label
signal_word, _event_label => _, VO_

## Result SVO
1. Then, {Back Office} [attaches] <the new SCT document>, and stores the expanded SCT physical file.
### Check Verbs => attaches
### {Back Office}, attaches, <the new SCT document>
### convert to active => {Back Office}, attaches, <the new SCT document>
### VO: attaches, <the new SCT document>
### Subject: {Back Office}

# ===================================
## Sentence 7
Ex : After that, some other MC internal staff receives the physical SCT file (out of scope).

## Start
1. Verb
verbs => [receives]
Ex: After that, some other MC internal staff [receives] the physical SCT file (out of scope).
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [some other MC internal staff]
Ex: After that, {some other MC internal staff} [receives] the physical SCT file (out of scope).
4. isConjVerb 
receives => False, 
5. Object
Ex: After that, {some other MC internal staff} [receives] <the physical SCT file> (out of scope).
verb, objs => receives, [the physical SCT file]
6. Label
signal_word, _event_label => _, VO_

## Result SVO
1. After that, some other MC internal staff receives the physical SCT file (out of scope).
### Check Verbs => attaches
### {Back Office}, attaches, <the new SCT document>
### convert to active => {Back Office}, attaches, <the new SCT document>
### VO: attaches, <the new SCT document>
### Subject: {Back Office}

# ===================================
# Group 3
# ===================================
## Sentence 1 (difficulty)
Ex : Each morning, the files which have yet to be processed need to be checked, to make sure they are in order for the court hearing that day.

## Start
1. Verb
verbs => [have, processed, checked, make, have, processed, are]
Ex: Each morning, the files which [[have]] yet to be [[processed]] need to be [checked], to [make] sure they [are] in order for the court hearing that day.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the files]
Subject => [need]
Ex: After that, Each morning, {{{the files}}} which [[have]] yet to be [[processed]] {{need}} to be [checked], to [make] sure they [are] in order for the court hearing that day.
4. isConjVerb 
have => False, 
processed => False
checked => False
make => False
are => False
5. Object
Ex: After that, Each morning, {{{the files}}} which [[have]] yet to be [[processed]] {{need}} to be [checked], to [make] sure they [are] in order for the court hearing that day.
verb, objs => have, []
verb, objs => processed, []
verb, objs => checked, []
verb, objs => make, []
verb, objs => processed, []
verb, objs => are, [order]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Result SVO 
1. Each morning, the files which [[have]] yet to be [[processed]] need to be [checked], to [make] sure they [are] in order for the court hearing that day.
### Check Verbs => have 
### {the files}, have, []
### convert to active => {the files}, have, []
### VO: have, []
### Subject: {the files}

### Check Verbs => processed 
### {the files}, processed, []
### convert to active => {}, processed, []
### VO: processed, []
### Subject: {}

### Check Verbs => checked 
### {the files}, check, []
### convert to active => {need}, check, []
### VO: check, []
### Subject: {need}

### Check Verbs => make 
### {}, make, []
### convert to active => {}, make, []
### VO: make, []
### Subject: {}

### Check Verbs => are 
### {}, are, []
### convert to active => {}, are, []
### VO: are, []
### Subject: {}

# ===================================
## Sentence 2
Ex : If some files are missing, a search is initiated, otherwise the files can be physically tracked to the intended location.

## Start
1. Verb
verbs => [missing, initiated, tracked]
Ex: If some files are [missing], a search is [initiated], otherwise the files can be physically [tracked] to the intended location.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [some files]
Subject => [a search]
Subject => [some files]
Ex: If {{some files}} are [missing], {a search} is [initiated], otherwise the files can be physically [tracked] to the intended 
4. isConjVerb 
missing => False, 
initiated => False
tracked => False
5. Object
Ex: {{some files}} are [missing], {a search} is [initiated], otherwise the files can be physically [tracked] to <the intended> 
verb, objs => missing, []
verb, objs => initiated, []
verb, objs => tracked, [the intended location]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

### Check Verbs => missing 
### {some files}, missing, []
### convert to active => {some files}, missing, []
### VO: missing, []
### Subject: {some files}

### Check Verbs => initiated 
### {a search}, initiate, []
### convert to active => [], initiate, {a search}
### VO: initiate, {a search}
### Subject: []

### Check Verbs => tracked 
### {some files}, tracked, []
### convert to active => [], track, {some files}
### VO: track, {some files}
### Subject: []

# ===================================
## Sentence 3
Ex : Once all the files are ready, these are handed to the Associate, and meantime the Judges Lawlist is distributed to the relevant people.

## Start
1. Verb
verbs => [are, handed, distributed]
Ex: Once all the files [are] ready, these are [handed] to the Associate, and meantime the Judges Lawlist is [distributed] to the relevant people.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [all the files]
Subject => [all the files]
Subject => [the Judges Lawlist]
Ex: Once {{all the files}} [are] ready, these are [handed] to the Associate, and meantime {the Judges Lawlist} is [distributed] to the relevant people.
4. isConjVerb 
are => False, 
handed => False
distributed => False
5. Object
Ex: Once {{all the files}} [are] ready, these are [handed] <to the Associate>, and meantime {the Judges Lawlist} is [distributed] to <the relevant people>.
verb, objs => are []
verb, objs => handed, [the Associate]
verb, objs => distributed, [the relevant people]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

### Check Verbs => are 
### {all the files}, are, []
### convert to active => {all the files}, are, []
### VO: are, []
### Subject: {all the files}

### Check Verbs => handed 
### {all the files}, handed, [the Associate]
### convert to active => [the Associate], hand, {all the files} 
### VO: hand, {all the files}
### Subject: {the Associate}

### Check Verbs => distributed 
### {the Judges Lawlist}, distributed, [the relevant people]
### convert to active => [the relevant people], distribute, {the Judges Lawlist} 
### VO: distribute, {the Judges Lawlist}
### Subject: [the relevant people]

# ===================================
## Sentence 4 (Fail)
Ex : Afterwards, the directions hearings are conducted.

## Start
1. Verb
verbs => [conducted]
Ex: Afterwards, the directions hearings are [conducted].
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the directions hearings]
Ex: Afterwards, {the directions hearings} are [conducted].
4. isConjVerb 
conducted => False
5. Object
Ex: Afterwards, {the directions hearings} are [conducted].
verb, objs => conducted, []
6. Label
signal_word, _event_label => _, VO_

### Check Verbs => conducted 
### {the directions hearings}, conducted, []
### convert to active => [], conduct, {the directions hearings} 
### VO: conduct, {the directions hearings} 
### Subject: []

# ===================================
# Group 4
# ===================================
## Sentence 1
Ex : After a claim is registered, it is examined by a claims officer

## Start
1. Verb
verbs => [registered, examined]
Ex: After a claim is [registered], it is [examined] by a claims officer.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [a claim]
Subject => [a claim]
Ex: After {{a claim}} is [registered], it is [examined] by a claims officer.
4. isConjVerb 
registered => False
examined => False
5. Object
Ex: After {{a claim}} is [registered], it is [examined] by <a claims officer>.
verb, objs => examined, [a claims officer]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 2
Ex : The claims officer then writes a “settlement recommendation”.

## NLP
nsubj  The claims officer
advmod then
ROOT writes
dobj a “settlement recommendation
punct ”
punct .

## Start
1. Verb
verbs => [writes]
Ex: The claims officer then [writes] a “settlement recommendation”.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [ The claims officer]
Ex: {The claims officer} then [writes] a “settlement recommendation”.
4. isConjVerb 
writes => False
5. Object
Ex: {The claims officer} then [writes] <a “settlement recommendation”>.
verb, objs => writes, [a “settlement recommendation]
6. Label
signal_word, _event_label => _, VO_

# ===================================
## Sentence 3
Ex : This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”.

## Start
1. Verb
verbs => [checked, mark]
Ex: This recommendation is then [checked] by a senior claims officer who may [mark] the claim as “OK” or “Not OK”.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [ This recommendation]
Subject => [who]
Ex: {This recommendation} is then [checked] by a senior claims officer who may [mark] the claim as “OK” or “Not OK”.
4. isConjVerb 
checked => False
mark => False
5. Object
Ex: {This recommendation} is then [checked] by <a senior claims officer> who may [mark] <the claim as “OK”> or “Not OK”.
verb, objs => checked, [a senior claims officer]
verb, objs => mark, [the claim, OK]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 4
Ex : If the claim is marked as “Not OK”, it is sent back to the claims officer and the recommendation is repeated. 

## Start
1. Verb
verbs => [marked, sent, repeated]
Ex: If the claim is [marked] as “Not OK”, it is [sent] back to the claims officer and the recommendation is [repeated]. 
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the claim]
Subject => [the claim]
Subject => [the recommendation]
Ex: If {{the claim}} is [marked] as “Not OK”, it is [sent] back to the claims officer and {the recommendation} is [repeated]. 
4. isConjVerb 
marked => False
sent => False
repeated => False
5. Object
Ex: If {{the claim}} is [marked] as “Not OK”, it is [sent] back to the claims officer and {the recommendation} is [repeated]. 
verb, objs => marked, [“]
verb, objs => sent, []
verb, objs => repeated, []
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 5
Ex : If the claim is OK, the claim handling process proceeds.

## Start
1. Verb
verbs => [is]
Ex: If the claim [is] OK, the claim handling process proceeds.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the claim]
Ex: If {the claim} [is] OK, the claim handling process proceeds.
4. isConjVerb 
is => False
5. Object
Ex: If {the claim} [is] OK, the claim handling process proceeds.
verb, objs => is, [the claim]
6. Label
signal_word, _event_label => _, VO_

# ===================================
# Group 5
# ===================================
## Sentence 1
Ex : When a claim is received, it is first checked whether the claimant is insured by the organization.

## Start
1. Verb
verbs => [received, checked, insured]
Ex: When a claim is [received], it is first [checked] whether the claimant is [insured] by the organization.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [a claim]
Subject => [a claim]
Subject => [the claimant]
Ex: When {{a claim}} is [received], it is first [checked] whether {the claimant} is [insured] by the organization.
4. isConjVerb 
received => False
checked => False
insured => False
5. Object
Ex: When {{a claim}} is [received], it is first [checked] whether {the claimant} is [insured] by <the organization>.
verb, objs => received, []
verb, objs => checked, []
verb, objs => insured, [the organization]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 2 (Fail)
Ex : If not, the claimant is informed that the claim must be rejected.

## Start
1. Verb
verbs => [informed, rejected]
Ex: If not, the claimant is [informed] that the claim must be [rejected].
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the claimant]
Subject => [the claim]
Ex: If not, {the claimant} is [informed] that {the claim} must be [rejected].
4. isConjVerb 
informed => False
rejected => False
5. Object
Ex: If not, {the claimant} is [informed] that {the claim} must be [rejected].
verb, objs => informed, []
verb, objs => rejected, []
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 3 (Fail)
Ex : Otherwise, the severity of the claim is evaluated.

## Start
1. Verb
verbs => [evaluated]
Ex: Otherwise, the severity of the claim is [evaluated].
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the severity]
Ex: Otherwise, {the severity} of the claim is [evaluated].
4. isConjVerb 
evaluated => False
5. Object
Ex: Otherwise, {the severity} of the claim is [evaluated].
verb, objs => evaluated, []
6. Label
signal_word, _event_label => _, VO_

# ===================================
## Sentence 4 (Fail)
Ex : Based on the outcome (simple or complex claims), relevant forms are sent to the claimant.

## Start
1. Verb
verbs => [Based, sent]
Ex: [Based] on the outcome (simple or complex claims), relevant forms are [sent] to the claimant.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => []
Subject => [relevant forms]
Ex: [Based] on the outcome (simple or complex claims), {relevant forms} are [sent] to the claimant.
4. isConjVerb 
Based => False
sent => False
5. Object
Ex: [Based] on <the outcome> (simple or complex claims), {relevant forms} are [sent] to <the claimant>.
verb, objs => Based, [the outcome]
verb, objs => sent, [the claimant]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 5 (Fail)
Ex : Once the forms are returned, they are checked for completeness.

## Start
1. Verb
verbs => [returned, checked]
Ex: Once the forms are [returned], they are [checked] for completeness.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the forms]
Subject => [they]
Ex: Once {the forms} are [returned], {they} are [checked] for completeness.
4. isConjVerb 
Based => False
sent => False
5. Object
Ex: Once {the forms} are [returned], {they} are [checked] for <completeness>.
verb, objs => returned, []
verb, objs => checked, [completeness]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 6 (Fail)
Ex : If the forms provide all relevant details, the claim is registered in the Claims Management system, which ends the Claims Notification process.

## Start
1. Verb
verbs => [provide, registered, ends]
Ex: If the forms [provide] all relevant details, the claim is [registered] in the Claims Management system, which [ends] the Claims Notification process.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the forms]
Subject => [the claim]
Subject => []
Ex: If {the forms} [provide] all relevant details, {the claim} is [registered] in the Claims Management system, which [ends] the Claims Notification process.
4. isConjVerb 
provide => False
registered => False
ends => False
5. Object
Ex: If {the forms} [provide] <all relevant details>, {the claim} is [registered] in <the Claims Management system>, which [ends] <the Claims Notification process>.
verb, objs => provide, [all relevant details]]
verb, objs => registered, [the Claims Management system]
verb, objs => ends, [the Claims Notification process]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 7
Ex : Otherwise, the claimant is informed to update the forms. 

## Start
1. Verb
verbs => [informed, update]
Ex: Otherwise, the claimant is [informed] to [update] the forms. 
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the claimant]
Subject => []
Ex: Otherwise, {the claimant} is [informed] to [update] the forms. 
4. isConjVerb 
provide => False
registered => False
ends => False
5. Object
Ex: Otherwise, {the claimant} is [informed] to [update] <the forms>. 
verb, objs => update, [the forms]
verb, objs => update, [the forms]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 7 (Fail)
Ex : Upon reception of the updated forms, they are checked again.

## Start
1. Verb
verbs => [checked]
Ex: Upon reception of the updated forms, they are [checked] again.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [they]
Ex: Upon reception of the updated forms, {they} are [checked] again.
4. isConjVerb 
checked => False
5. Object
Ex: Upon reception of the updated forms, {they} are [checked] again.
verb, objs => checked, []
6. Label
signal_word, _event_label => _, VO_

# ===================================
# Group 6
# ===================================
## Sentence 1
Ex : The Police Report related to the car accident is searched within the Police Report database and put in a file together with the Claim Documentation. 

## Start
1. Verb
verbs => [related, searched, put]
Ex: The Police Report [related] to the car accident is [searched] within the Police Report database and [put] in a file together with the Claim Documentation. 
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => []
Subject => [ The Police Report]
Subject => []
Ex: {The Police Report} [related] to the car accident is [searched] within the Police Report database and [put] in a file together with the Claim Documentation. 
4. isConjVerb 
related => False
searched => False
put => False
5. Object
Ex: {The Police Report} [related] to <the car accident> is [searched] within <the Police Report database> and [put] in <a file together with the Claim Documentation>. 
verb, objs => related, [the car accident]
verb, objs => searched, [the Police Report database]
verb, objs => put, [a file, the Claim Documentation]
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 2
Ex : This file serves as input to a claims handler who calculates an initial claim estimate.

## Start
1. Verb
verbs => [serves, calculates]
Ex: This file [serves] as input to a claims handler who [calculates] an initial claim estimate.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [ This file]
Subject => [who]
Subject => []
Ex: {This file} [serves] as input to a claims handler {who} [calculates] an initial claim estimate.
4. isConjVerb 
serves => False
calculates => False
5. Object
verb, objs => serve, [input]
verb, objs => calculates, [an initial claim estimate]
Ex: {This file} [serves] as <input> to a claims handler {who} [calculates] <an initial claim estimate>. 
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 3
Ex : Then, the claims handler creates an Action Plan based on an Action Plan Checklist available in the Document Management system.

## Start
1. Verb
verbs => [creates, based]
Ex: Then, the claims handler [creates] an Action Plan [based] on an Action Plan Checklist available in the Document Management system.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => [the claims handler]
Subject => []
Ex: Then, {the claims handler} [creates] an Action Plan [based] on an Action Plan Checklist available in the Document Management system.
4. isConjVerb 
creates => False
based => False
5. Object
verb, objs => creates, [an Action Plan]
verb, objs => based, [an Action Plan Checklist]
Ex: Then, {the claims handler} [creates] <an Action Plan> [based] on <an Action Plan Checklist> available in the Document Management system.
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 4
Ex : Based on the Action Plan, a claims manager tries to negotiate a settlement on the claim estimate.

## Start
1. Verb
verbs => [Based, tries, negotiate]
Ex: [Based] on the Action Plan, a claims manager [tries] to [negotiate] a settlement on the claim estimate.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => []
Subject => [a claims manager]
Subject => []
Ex: [Based] on the Action Plan, {a claims manager} [tries] to [negotiate] a settlement on the claim estimate.
4. isConjVerb 
Based => False
tries => False
negotiate => False
5. Object
verb, objs => Based, [the Action Plan]
verb, objs => negotiate, [a settlement]
potential_new_verb, potential_new_objs => negotiate [a settlement]
verb, objs => negotiate, [a settlement]
Ex: [Based] <on the Action Plan>, {a claims manager} [tries] to [[negotiate]] <<a settlement>. on the claim estimate.
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

# ===================================
## Sentence 5
Ex : The claimant is informed of the outcome, which ends the process.

## Start
1. Verb
verbs => [informed, ends]
Ex: The claimant is [informed] of the outcome, which [ends] the process.
2. Add sequence (follow from verbs)
self.sequence += 1
3. Subject (Subject more than 1 extend)
Subject => []
Subject => [a claims manager]
Subject => []
Ex: {The claimant} is [informed] of the outcome, which [ends] the process.
4. isConjVerb 
informed => False
ends => False
5. Object
verb, objs => informed [the outcome]
verb, objs => ends [the process]
Ex: {The claimant} is [informed] of <the outcome>, which [ends] <the process>.
6. Label
signal_word, _event_label => _, VO_
signal_word, _event_label => _, VO_

## Conclusion
## Add Step
1. ตัดประโยค 
|{The claimant} is [informed] of <the outcome>, which [ends] <the process>.|
2. ถ้าเป็นประโยคที่มี Subject 1 ตัว 
|{The claimant} is [informed] of <the outcome>, which [ends] <the process>.|