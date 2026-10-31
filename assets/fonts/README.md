# Homepage fonts

Both languages use Noto Sans SC, hosted locally as WOFF2 subsets at weights
400 and 600. Latin and Chinese glyphs come from the same family. Icons and
mathematical notation retain their specialized fonts.

The SIL Open Font License is included in OFL-NotoSansSC.txt.

Official source files (Google Fonts Noto Sans SC v41):

- Regular: https://fonts.gstatic.com/s/notosanssc/v41/k3kCo84MPvpLmixcA63oeAL7Iqp5IZJF9bmaG9_FnYw.ttf
- Semibold: https://fonts.gstatic.com/s/notosanssc/v41/k3kCo84MPvpLmixcA63oeAL7Iqp5IZJF9bmaGwHCnYw.ttf
- License: https://github.com/google/fonts/blob/main/ofl/notosanssc/OFL.txt

After adding Chinese text, run `scripts/build_fonts.py` with these two downloaded
TTFs and commit the rebuilt WOFF2 files. The script includes Latin characters
and the website's current text. Uncovered characters fall back to the configured
system Chinese fonts and remain readable. Install `fonttools` and `brotli` to
rebuild; visitors and GitHub Pages need neither dependency.
