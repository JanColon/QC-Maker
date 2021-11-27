# Short Description
A tool to streamline .QC file production for model creation in the Source Engine

![Software Demo Gif](https://media0.giphy.com/media/UDCAPTTLkHMZsso2sY/giphy.gif "Demo")

# Longer Description
When creating models for use in the source engine, the models require a QC file in order to compile all necessary info and produce a functional .mdl file for modding use. The .QC file creation process is tedious and *sometimes* time consuming depending on the custom model's complexity. In an effort to streamline the QC creation process for the sake of simplicity and swiftness, I created QC Maker.

# What's a QC file?
The Source Engine uses .mdl files to process props, NPCs and more. Because of the numerous factors that go into making a complete model (textures paths, sequences, etc...) the Source Engine uses .QC files as a manifest of every detail necessary for the model. After the QC has been written, it goes through a compiler and a usable .mdl file is ready for use in Source.

# Features (as of release 1.0)
- Create uniquely-named .QC files
- Open different .QC files to edit individually
- Create unique name/pathname for .mdl files ($modelname)
- Apply a reference mesh ($body) ($bodygroups not yet added)
- Apply material path(s) ($cdmaterials)
- Apply sequences (really basic) (advanced options not yet implemented) ($sequence)
- Apply collision models (really basic) (only adds $concave by default) ($collisionmodel)
- Apply hitboxes ($hbox)
- Apply static model property ($staticprop)

# Requirements
- Windows 10 (for general users) (sorry Mac & Linux users)
- Python 3.9+ (for development)

# Special Thanks to...
- Valve Developer Community (providing documentation on QC files)
- Stack Exchange (saving me from going insane due to the simplest of issues)
