# First-run prompt: Microsoft images on the VM (MAI Image 2.7)

**CLOSED 21.11.2026: do not run.** Tested once on the VM; Marko judged the pictures worse than Google's and asked
to stop spending credits. Kept only as a record.

Paste the whole box below as the first message of a Claude Code session **running on chromium-vm**. Written
21.11.2026 in a cloud session that could not reach the VM, the private manifest or microsoft.ai, so the skill
and the manifest module it points to are drafts: this run is what tests them.

```text
TASK: first run of Microsoft images (MAI Image 2.7 in MAI Labs) on this machine.

Marko's words, 21.11.2026:
"Please try, test and write the skills and manifests. Mantra manifest also. We can start now experimenting in
my own virtual machine with this."
"Instead of generating image for my therapist markobosko.com, generate same image with Microsoft, put there in
my bookmarks that site in the bookmark bar in my virtual machine and show me in this chat comparison between
Google images and Microsoft images of the same subject as we did on the page."

Write those words into momentaryupdates.md of vm-chromium before anything else.

0. Read skill this-machine. Clone or pull markoboskoauroville/APPS_MIND_MAP, branch ccr-482c2716-sskhhf
   (or main once merged). Read skills/microsoft-images/SKILL.md and manifest/microsoft-image-jobs.md.

1. INSTALL THE SKILL
   - Copy APPS_MIND_MAP/skills/microsoft-images/ to ~/vm-chromium-git/.claude/skills/microsoft-images/ and
     symlink ~/.claude/skills/microsoft-images to it, the way this-machine is linked.
   - Run the tool's own test: make two folders with one same-named picture each and run compare.py; it must
     write the pair, sheet.jpg and comparison.html.

2. OPEN MAI LABS
   - In the Linux Chrome open https://microsoft.ai/news/introducing-mai-image-2-7/ and follow its MAI Labs link.
   - If a Microsoft sign-in appears, stop and ask Marko to sign in himself in the viewer. Never type a
     password, create an account or accept terms for him.
   - Bookmark MAI Labs in the bookmarks bar of that Chrome profile (skill section 6) and make the bar visible.
     Tell Marko the title and address added.

3. THE SAME PICTURES WITH MICROSOFT
   - Subjects: the pictures of the therapies site that were made in Gemini. Start with two: room and setup
     (repo MARKOBOSKO_THERAPIES, site/img/room.jpg and setup.jpg; prompts on Drive in
     Chromium Downloads/Gemini/_batch/batch-markobosko-therapies*.json). Ask Marko before doing the rest.
   - For each: the exact Gemini prompt, 16:9, model MAI Image 2.7, one picture per prompt. Then once more with
     Flash for room only, to see the difference between the two Microsoft models.
   - Save and name by skill section 5. Note the seconds each took and any limit or refusal notice, word for word.

4. COMPARE AND SHOW
   - Google pictures in one folder as "<subject> (nano banana).png", Microsoft ones in another, then compare.py.
   - Show sheet.jpg in this chat as an image, then the counted findings per pair (skill section 7).
   - Do not change the therapies site. Publishing a Microsoft picture there waits for Marko's word and for the
     answer on business use (manifest module, rule 9).

5. WRITE BACK WHAT WAS LEARNED
   - In SKILL.md replace every FIRST RUN mark with what was seen: the MAI Labs and Canvas addresses, the
     sign-in account, the aspect ratios offered, the free limit, download versus screenshot, watermark or
     Content Credentials, which bookmark road worked. Add lessons with the date.
   - Read Microsoft's terms for MAI Labs and write the answer on business use into the manifest module.
   - Push the skill to vm-chromium. Copy manifest/microsoft-image-jobs.md into MANTRA_MANIFEST as
     modules/microsoft-image-jobs.md, fit it to the manifest's layout, add it to the module list, push.
   - In APPS_MIND_MAP add the task "generate images in Microsoft MAI Image 2.7 (MAI Labs)" to the vm-chromium
     record in data/apps.json, run python3 tools/build_map.py twice, push.

Stop and ask Marko when: a sign-in or payment page appears, the free limit is reached, or a result shows a
real person's face that was not in the prompt.
```
