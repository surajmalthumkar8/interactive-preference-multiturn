# House style for reason fields — the binding rule

Derived by reading five signed-off tasks in campaign `5b853679` (the same campaign and the
same model pairing as current work): tasks 015, 048, 079, 054, 018. Fifteen approved reason
fields in total. Where this file and any older note disagree, **this file wins**, because it
is taken directly from work the client signed off.

## The rule

**Write the reason the way a person who just looked at both pages would explain their choice
to a colleague. Describe what you saw. Never report what you measured.**

## What the approved corpus does

### 1. The opener is always the plain form

Every one of the fifteen fields opens `Website A is better because ...` or
`Website B is better because ...`. Two variants appear and both are fine:

- `Website A is better overall because ...` (overall lens only, used in 079 and 054)
- `Website A and Website B are tied because ...` (when the verdict is Both are bad, 079)

**Never** write "is better visually because" or "is better functionally because." The lens is
already the question; saying it back is not how the approved work reads. Note `validate_reasons.py`
anchors on `^website a is better`, so the plain form passes the validator too.

### 2. No numbers from instruments. Ever.

Not one of the fifteen fields contains a pixel count, a sampled value, a frame reading, or any
figure that could only come from a devtools console. This is the single biggest tell that
separates a machine-written reason from an approved one.

Approved phrasing describes the same defect in seen terms:

> "both front and rear wheels floating away from the underside with a visible gap, and several
> flat panels, including a gray plank and an orange slab, sitting disconnected in midair"

> "each row stacks eight bars inside a space too short for them, so the lower bars in every row
> spill past the row's border and crowd into the row beneath"

Measure privately to be sure you are right. Then throw the numbers away and write what the
measurement means to someone looking at the page. Figures that a **viewer can read off the page
itself** (a headline percentage, a price, a label) are fine, because a person sees those.

### 3. Write from the viewer's side

Approved fields talk about what a person can do and see:

> "it lets a person actually turn and approach the car, while Website A does not move at all"
> "a viewer can see the whole house"
> "a viewer who opens Website B is left with an empty coloured field and no way in at all"

Not about what the page technically contains.

### 4. Length: 90 to 160 words, most near 100

Measured: 94, 93, 94, 118, 158, 147, 102, 92, 98, 121, 136, 111. The centre of mass is around
100 to 120. Do not pad toward 150 to look thorough. Say the thing and stop.

### 5. Name the winner's flaw, plainly

Nearly every approved field concedes. The approved tone is blunt about it:

> "Its own flaws are plain: the land reads as flat green shapes rather than continents, the gold
> routes stop in open space, and a hard grey rectangle sticks out from behind the sphere."

> "Website B's own build has a real weakness, with its wheels and a few flat panels sitting apart
> from the body instead of meeting it, but it is still the one that lets a person look the car over."

### 6. Close with a short human verdict line

> "A complete image beats a handsome fragment."
> "a page that shows part of the request beats one that shows none of it."
> "That gap decides the question on its own."

### 7. State ties honestly

Task 079 recorded Both are bad and opened `Website A and Website B are tied because each one
fails a different part of the request.` Do not force an A/B pick when the evidence says tie.

## The one thing to check before submitting

Read the three reasons back. If any sentence could only have been written by something with a
console open, rewrite that sentence. That is the test.

## Functionality means functionality AND instruction following

Client clarification, 2026-09-09. Both halves count, and they are weighted.

**When both candidates are effectively static there is nothing to exercise, so the whole
functionality judgement becomes which one follows the prompt better.** Do not pad the field
with control-by-control notes when there are no controls worth the words.

**Everything present gets tested, requested or not.** If the prompt asked for an image and a
candidate added a download button nobody asked for, that button gets clicked. Unrequested
features are still part of the build and still break.

**Explicitly requested beats self-added.** A candidate that answers the prompt well and ships
a broken extra beats one that answers the prompt poorly and ships a working extra. Worked
example from the client: the prompt asks for an image, Website A gives a good image plus a
broken download button, Website B gives a poor image plus a working download button. Website A
wins, and the reason says so plainly: Website A follows the request better even though its
extra button is broken, while Website B has the working button but does not answer the request.

Rank the evidence that way before writing. A long list of working controls does not outweigh
missing the thing that was actually asked for.

## Do not submit in under ten minutes

Client reminder, 2026-09-09. A task submitted in under ten minutes reads as not fully
reviewed, and submission time is one of the first things the audit looks at. The inspection
this project asks for does not fit in less than that anyway: two sites, every section, every
control exercised, then three reasons drafted and gated. If the clock says eight minutes,
something was skipped.
