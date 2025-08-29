# Contributing Guideline

## Adding a new language of Chinese

::: warning

`<ISO 639-3 language code>` is normally must used. If there are several specified language type, append a tag and join the code and tag with a hypen, like:

`<language-code>-<tag>`

The `<tag>` can be either an ISO-639-6 code or a customized tag.

:::

For creating a layout that belong to a language not existing in this project, one should:
- Create a new folder with the folder name `lang-<ISO 639-3 language code>`.
- Create a new `info.spellconvert.info` inside this folder, which contains the information of tonal scheme that new layouts being supported, and the middle form of the tones of this language.
  - The file should include:
    - Supported layout or romanized/tone-marking standard
    - The chart of standard middle form, no matter standarized or historical - it is up to the range you want to support
- Create a new `lib.babel-<ISO 639-3 language code>` which contains the converting rules between the spelling form and the middle form.
- Create a new `lib.scribe-<ISO 639-3 language code>` which contains the forms changing between typing form and the existing form.
- For schemas, the name should be `rscm.<layout name>`.
- Create a new `README-<ISO 639-3 language code>` to indicating how this language being used.

## Creating an issue

Inside the issue you must provide information below:
- The dictionary you are using
- The layout schema you are using
- the typing you expected to see
- the typing you actually get
