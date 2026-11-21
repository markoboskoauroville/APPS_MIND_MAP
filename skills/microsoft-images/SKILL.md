---
name: microsoft-images
description: How a Claude session on the Linux VM chromium-vm makes pictures with Microsoft's MAI Image 2.7 and MAI Image 2.7 Flash in MAI Labs (browser, Microsoft sign-in, no Azure), saves them, and puts them next to the Google (Gemini, Nano Banana) picture of the same subject. Read it before any Microsoft image, any "same image with Microsoft", any Google-versus-Microsoft comparison, and before bookmarking a site in the VM's Chrome. Update it with every lesson.
---

# Microsoft images on chromium-vm (MAI Image 2.7 in MAI Labs)

**CLOSED 21.11.2026.** Marko, after the first pictures: *"Images are not as good as Google. Please don't spend my
credits anymore. Stop all tasks and close the project."* Gemini (Nano Banana) stays the only image maker. Do not
use MAI Labs or any paid Microsoft image road unless Marko asks for it again in his own words. The notes below are
kept for that case.

Status 21.11.2026: **written in a cloud session that could not reach the VM or microsoft.ai.** Sections marked
CHECKED are confirmed; sections marked FIRST RUN are the plan and must be corrected by the first session that
runs them on the VM. Read skill `this-machine` first: every rule there (this VM only, the Linux Chrome, files
and Drive, text answers) applies here too.

## 1. What it is (CHECKED from Microsoft's pages through web search, 21.11.2026)

- Two models, released 17.11.2026: **MAI Image 2.7** (final pictures, first place for image editing on Artificial
  Analysis, about $35 per 1,000 through the API) and **MAI Image 2.7 Flash** (fast drafts, about $10 per 1,000).
- **MAI Labs** is Microsoft's browser playground for both. No Azure, no paid plan; a Microsoft account sign-in.
  Stated by a third-party guide, not yet read on Microsoft's own terms: personal, non-commercial use, adults only.
- **Canvas** (inside MAI Labs, runs on Flash, limited preview): prompt column on the left, picture on the right,
  a switch between "New image" and "Diagram", select a region to replace, move or restyle. One picture per prompt,
  about 10 to 20 seconds.
- Limits of the model: up to 4,194,304 pixels (2048x2048, or wider with the same total), PNG, JPEG or WebP,
  transparent backgrounds, reference-image editing.
- Paid roads, only when Marko asks: Microsoft Foundry (`MAI-Image-2.7`, `MAI-Image-2.7-Flash`, version
  2026-11-02, Global Standard), OpenRouter, fal, Vercel (`microsoft/mai-image-2.7`, `microsoft/mai-image-2.7-flash`).
- Not known yet: the free daily limit in MAI Labs, whether results carry a visible watermark or Content
  Credentials. Write both here when seen.

## 2. When to use which maker

- Marko says "with Microsoft", "MAI", "same image with Microsoft": this skill.
- Marko says nothing about the maker: Gemini (Nano Banana) stays the default, manifest module
  `gemini-image-jobs.md` and skill `this-machine` section 4.
- A comparison needs both: make the Google one by the Gemini rules, the Microsoft one by these, with the
  **same prompt text and the same aspect ratio**. Change nothing else between the two.
- Site pictures for a business (markobosko therapies, Elevate Media): MAI Labs may be non-commercial only.
  Until that is read on Microsoft's terms page, a Microsoft picture is for comparison, not for publishing.
  Tell Marko this once when he asks to publish one.

## 3. Open and sign in (FIRST RUN)

1. Linux Chrome on this VM, the profile Marko names (default: the one that makes the Gemini pictures).
2. Open MAI Labs. Seen by the VM session vm1 on 21.11.2026 (read-only visit, not signed in):
   - MAI Labs: `https://labs.microsoft.ai/?model=mai-image-2-7-flash` (the `model` value picks the model).
     Canvas: `https://labs.microsoft.ai/?model=canvas`. Page title "MAI Labs | Microsoft AI".
   - The page: a cookie banner (Accept, Reject, Manage), "Sign in" at the top right, a prompt box "What do
     you want to create?" with a + button, a model picker (default MAI-Image-2.7-Flash) and Send; a bottom
     bar with MAI-Image-2.7, voice and chat. Footer: "MAI Labs is a limited preview of new and experimental
     AI models."
   - The VM's Chrome was not signed in to Microsoft. The cookie banner is Marko's choice too: ask him.
   - The launch post says nothing about regions, age, free limits or business use.
3. If a Microsoft sign-in page appears, **stop and ask Marko in the chat to sign in himself** in the VM viewer.
   Never type a password, never create an account, never accept terms for him. After he signs in, read the
   account name shown in the page and tell him which account is in use.
4. Bookmark it (section 6) so the next session starts from the bar.

## 4. Make one picture (FIRST RUN, same discipline as Gemini)

1. One picture per prompt, one subject per run. Pick the model on purpose: **2.7** for a picture Marko keeps,
   **Flash** for drafts and for Canvas edits. Say which one was used.
2. Set the aspect ratio before sending (site hero pictures are 16:9, Suno covers 1:1) and read it back from
   the page after setting it.
3. Paste the prompt exactly as given to Gemini when this is a comparison. Keep the prompt text in a file next
   to the result (`<name>.prompt.txt`).
4. Wait for the result with page state, not with a fixed sleep: no spinner, an `img` with natural width of 700
   or more. Read the page text for a limit or refusal notice before retrying; never loop on a refusal.
5. Check the picture against the prompt (count the people, the speakers, the walls) before showing it.
6. A reference picture (editing): attach it through the page's upload control. If only paste works, use the
   Gemini trick from `this-machine` section 4 (temporary file input, then a paste event). Record which worked.

## 5. Save and name

- Save at natural size. First choice on this site is the page's own download control **if** it gives the full
  file; if it gives a smaller or recompressed file, save by screenshot as for Gemini (overlay at natural size,
  capture 1:1). Write here which one is right after comparing the two once.
- Name: `<subject> (mai image 2.7).png` or `<subject> (mai image 2.7 flash).png`. The Google twin is
  `<subject> (nano banana).png`. `compare.py` pairs files by the name before the bracket.
- Drive: `My Drive / Mantra References / <PROJECT> (Microsoft - MAI Image in Chrome) / references | results`,
  next to the project's Gemini folder. Tell Marko the full Drive path every time.

## 6. Bookmark a site in the VM's Chrome bookmarks bar (FIRST RUN)

A page script cannot touch Chrome's own bookmarks (LESSONS 2.11.2026). Two roads that can:

1. **A `chrome://bookmarks` tab through DevTools** (the same way prefs were set through `chrome://settings`):
   open the tab, then evaluate
   `chrome.bookmarks.search({url: U}, r => r.length || chrome.bookmarks.create({parentId: '1', title: T, url: U}))`.
   Parent `'1'` is the bookmarks bar. The search first keeps it from being added twice.
2. **Keys through vm-agent** when road 1 is refused: bring the tab to the front, `key ctrl+d`, check with a
   screenshot that the folder says "Bookmarks bar", `key Return`.

Then make the bar visible: `ctrl+shift+b` toggles it, so look at a screenshot first and press only if it is
hidden. Bookmarks sync to every device of that Chrome profile's account: add only what Marko asked for, in
the profile he named, and tell him the title and address added.

## 7. Compare Google and Microsoft (CHECKED: the tool, on stand-in pictures)

`compare.py` in this folder (needs ImageMagick, already on the VM):

```
python3 ~/.claude/skills/microsoft-images/compare.py <google_dir> <microsoft_dir> <out_dir> --title "Therapy room"
```

- Writes one side-by-side JPEG per pair (same height, maker and model under each), `sheet.jpg` with all pairs,
  and `comparison.html`. Lists pictures that have no partner. Exit 1 when there is no pair.
- Show Marko `sheet.jpg` in the chat, then say in plain words, per pair: which follows the prompt better,
  which looks more like a photograph, faces and hands, any text in the picture, and the time each took.
  Count things; do not give marks out of ten for taste. Marko chooses.
- For a web page (as on markoboskotherapies), publish the pair pictures, never the raw originals at full size.

## 8. Mistakes and lessons

None yet. Add each with its date and Marko's words, then commit and push (section 9).

## 9. Keep this skill current

Lives in `markoboskoauroville/vm-chromium` under `.claude/skills/microsoft-images/` (live copy
`~/.claude/skills/microsoft-images`, a symlink, like `this-machine`). The draft was written in
`markoboskoauroville/APPS_MIND_MAP`, folder `skills/microsoft-images/`. After the first run on the VM,
replace every FIRST RUN mark with what was seen, and update the manifest module `microsoft-image-jobs.md`.
