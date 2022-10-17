<h1 align="center">
  <br>
  <a href="https://github.com/BobEXP/ChayaV2"><img src="https://i.ibb.co/X2WmCxm/chaya.png" alt="ChayaV2"></a>
  <br>
  ChayaV2
  <br>
</h1>

<p align="center">
  <a href="https://github.com/BobEXP/ChayaV2">
    <img src="https://img.shields.io/badge/release-v2-green">
  </a>
   </a>
  <a href="https://github.com/BobEXP/ChayaV2/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-AGPL3-_red.svg">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/language-python3-green">
  </a>
</p>

<h3 align="center">Right To Privacy</h3>

**Chaya** protects your privacy through steganography, cryptography and compression. It effectively encrypts your payloads using *AES-256-GCM* cryptography, embeds them using *LSB-LPS* steganography technique into images and compresses them using *FLIF* to evade detection by performing lossless compression. 

ChayaV2 is for your privacy backed by research.

**WHY CHAYA-V2 IS BETTER THAN THE REST?**

- [x] 0% detection rate using most of the publically available anti-steg tools like stegexpose and many more
- [x] 100% data retention with almost the same capacity of standard LSB technique with LBS-LPS
- [x] Transparent cryptography that gets as good as python has to offer

***There is no way this can be broken using a standard supercomputer unless there are exploits in python libs and python itself.. LSB-LPS will take exponetially large time to brute-force with larger graph images because you will have to attack every X,Y coordinates combo without any error. Making an ML to do so is also quite useless and can be only used for Natural language processing for example: which message is readable to find the coordinates. AFTER THAT, you have to break the encryption. MOREOVER, NLP ML cannot find the coordinates because the bruteforce results will be ciphertext anyway. If for some reason the attacker knows the coordinates to start the de-steg process, they will have to break AES-GCM-256. GCM is better because it offers integrity along with confidentiality, which is why it's the better AES mode).***

<strong><a href="https://www.un.org/en/about-us/universal-declaration-of-human-rights">United Nations Declaration of Human Rights (UDHR) 1948, Article 12 - </strong></a>“No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honor and reputation. Everyone has the right to the protection of the law against such interference or attacks.”
<br><br>
<strong><a href="https://en.wikipedia.org/wiki/International_Covenant_on_Civil_and_Political_Rights">International Covenant on Civil and Political Rights (ICCPR) 1966, Article 1 - </strong></a>"No one shall be subjected to arbitrary or unlawful interference with his privacy, family, home or correspondence, nor to unlawful attacks on his honor or reputation. Everyone has the right to the protection of the law against such interference or attacks."


## Features v2

<p align="center" >
    <img src="https://raw.githubusercontent.com/BobEXP/ChayaV2/main/assets/ChayaV2_Banner.png" alt="ChayaV2">
</p>

- [x] **Encryption**: AES-256-GCM *(default - best)*
- [x] **Steganography Mode**: Least Significant Bit (LSB)
- [x] **Steganography Mode**: Least Significant Bit + Random Linked Pixels (LSB-LPS) *(default - best)*
- [x] **Encoding Architecture**: Encode One/Single Image
- [x] **Encoding Architecture**: Encode Multiple Images With Same Payload *(default)*
- [x] **Encoding Architecture**: Split Encode Payload Into Linear Chains of Multiple Images
- [x] **Encoding Architecture**: Split Encode Payload Into Random Chains of Multiple Images *(best)*
- [x] **Execution Mode**: Execute payload from Memory without saving on disk *(git rekt victim)*
- [x] **Execution Mode**: Execute payload after saving to temprary file on disk *(git detected attacker)*
- [x] **Standard Option**: JSON to CSV conversion
- [x] **Standard Option**: JPG to PNG conversion
- [x] **Standard Option**: Easy clear app data
- [x] **Standard Option**: Easy updater
- [x] **Standard Option**: Verbose help


### Changelog v2

Changelog: https://github.com/BobEXP/ChayaV2/blob/main/CHANGELOG.md

## Install

## Windows

- Download project from github, extract & run!

*OR* run in CMD:

```bash
git clone --depth=1 https://github.com/BobEXP/ChayaV2
```

## Linux

### One Line Setup

Use the following command for faster setup:

**Command For Ubuntu Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/BobEXP/ChayaV2.git && cd ChayaV2 && pip3 install -r requirements.txt && sudo apt update && sudo apt-add-repository ppa:linuxuprising/libpng12 && sudo apt update && sudo apt install -y libpng12-0
```

**Command For Debian Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/BobEXP/ChayaV2.git && cd ChayaV2 && pip3 install -r requirements.txt && sudo apt update && sudo apt install build-essential devscripts && cd ~/ && sudo touch /etc/apt/sources.list.d/libpng12.list && echo "deb https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && echo "deb-src https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 1CC3D16E460A94EE17FE581CEA8CACC073C3DB2A && sudo apt update && sudo apt install -y libpng12-0
```

### Using installer.py

You can install the dependencies using installer.py script. Run the following commands in terminal:

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/BobEXP/ChayaV2.git && cd ChayaV2
````

**Ubuntu Based Distros**
```shell
python3 installer.py --ubuntu
````

**Debian Based Distros**
```shell
python3 installer.py --debian
````

If installer.py has issues, try to run the one line setup command.


## Usage

### Help Menu

```shell
python3 chaya.py --help
```

### Automatic Operations

#### Clear all data - clean the folders

```shell
python chaya.py -cleardata
```

#### Add images

You must add the image(s) to `/autoexp/raw_images/` folder that you want to steg.

If your images are in JPEG format, you can convert them using the following command along with passing your other commands:

```shell
python chaya.py -jpg2png -enc -m "powershell.exe some command here as your payload here" -amlchi
```

#### View cipher data

You may confirm the steg data and other sensitive information inside `/appdata/cipher_data.json`.

#### Decrypt and run payload in memory

One of the execution options allows you to run the embed payload right after de-steg process while it's in the memory! To do this:

```shell
python chaya.py -dec -amlchi -exmem
```

#### Compression

Only works for Linux - not tested extensively! 

#### Guided Demo v2

<p align="center" >
    <img src="https://raw.githubusercontent.com/BobEXP/ChayaV2/main/assets/video_banner.png" alt="ChayaV2 Demo">
</p>

### Output Data

- Enc + Steg images -> /autoexp/image_steg/
- Enc + Steg + Comp images -> /autoexp/image_steg_comp/
- Cipher data -> /appdata/cipher_data.json
- Analysis data -> /appdata/analysis_results_enc.json (suspended)


### Issues - v2

- Updater Fix
- Update check fix


## License

ChayaV2 is licensed under <a href="https://github.com/BobEXP/ChayaV2/blob/main/LICENSE">AGPLv3</a>


## Support ChayaV2

Find me and give C@$H
