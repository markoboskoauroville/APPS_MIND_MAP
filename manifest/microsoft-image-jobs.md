# Microsoft image jobs (MAI Image 2.7 in MAI Labs)

Draft module for `markoboskoauroville/MANTRA_MANIFEST`, file `modules/microsoft-image-jobs.md`, the twin of
`modules/gemini-image-jobs.md`. Written 21.11.2026 in a cloud session that could not open the private manifest,
so the layout follows the public documents of the account, not the manifest's own modules: fit the headings to
the manifest when it is copied in, and add it to the module list in START_HERE.md.

Marko, 21.11.2026 (typed): *"Please try, test and write the skills and manifests. Mantra manifest also. We can
start now experimenting in my own virtual machine with this."*

## The rule

1. **Google stays the default.** A picture with no maker named is made in Gemini (Nano Banana) by
   `gemini-image-jobs.md`.
2. **Microsoft when Marko says so** ("with Microsoft", "MAI", "the same image with Microsoft"): MAI Image 2.7
   or MAI Image 2.7 Flash in **MAI Labs**, in the browser, with Marko's Microsoft sign-in. No Azure, no API key,
   no paid plan unless Marko asks for one in his own words.
3. **Where:** the Linux VM chromium-vm and its Chrome, by the skill `microsoft-images` in
   `vm-chromium/.claude/skills/`. Not the Mac, unless Marko names the Mac for that task.
4. **Sign-in is Marko's.** A session never types a password, creates an account or accepts terms. It stops and
   asks him to sign in, then reads back which account is in use.
5. **One picture per prompt.** 2.7 for pictures that are kept, Flash for drafts and Canvas edits. The model is
   named in the file name and in the answer.
6. **A comparison changes one thing only:** the maker. Same prompt text, same aspect ratio, same references.
7. **Names:** `<subject> (mai image 2.7).png`, `<subject> (mai image 2.7 flash).png`; the Google twin is
   `<subject> (nano banana).png`. The prompt is kept beside the result as `<subject>.prompt.txt`.
8. **Drive:** `My Drive / Mantra References / <PROJECT> (Microsoft - MAI Image in Chrome) / references | results`.
   The full path is told to Marko every time.
9. **Publishing:** MAI Labs is reported as personal, non-commercial use. Until a session has read that on
   Microsoft's own terms page and written the answer here, a MAI Labs picture is shown to Marko and compared,
   not published on a business site. A published Microsoft picture goes through a paid road (Foundry, OpenRouter,
   fal, Vercel) that Marko has approved.
10. **Showing a comparison:** side by side, the same height, the maker and model under each picture
    (`compare.py` in the skill). Findings are counted facts (people, objects, text, time taken), not marks for
    taste. Marko chooses.

## Facts (21.11.2026, from Microsoft's pages through web search)

- Released 17.11.2026. Public preview. MAI Image 2.7 about $35 per 1,000 pictures, Flash about $10 per 1,000.
- Up to 4,194,304 pixels (2048x2048 or the same total in another shape), PNG, JPEG, WebP, transparent
  backgrounds, reference-image editing.
- Canvas in MAI Labs runs on Flash: prompt left, picture right, "New image" or "Diagram", region select to
  replace, move or restyle; limited preview.
- Foundry ids `MAI-Image-2.7` and `MAI-Image-2.7-Flash` (version 2026-11-02, Global Standard); gateway ids
  `microsoft/mai-image-2.7` and `microsoft/mai-image-2.7-flash`.

## Not yet known (fill in after the first run on the VM)

- The MAI Labs and Canvas addresses, the free daily limit, the aspect ratios the page offers.
- Whether the download control gives the full file, and whether results carry a watermark or Content Credentials.
- Whether Microsoft's terms allow business use of MAI Labs pictures.

## Where things are

- Skill and comparison tool: `vm-chromium/.claude/skills/microsoft-images/` (draft in
  `APPS_MIND_MAP/skills/microsoft-images/`).
- First-run prompt for a VM session: `APPS_MIND_MAP/prompts/MICROSOFT_IMAGES.md`.
- Sources: microsoft.ai/news/introducing-mai-image-2-7, microsoft.ai/models/mai-image-2-7,
  microsoft.ai/pdf/MAI-Image-2.7-Model-Card.pdf,
  learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-mai-image.
