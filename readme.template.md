<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** kajuberdut, incase, twitter_handle, patrick.shechet@gmail.com, incase, String functions in pure Python
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/kajuberdut/incase">
    <img src="https://raw.githubusercontent.com/kajuberdut/incase/main/images/icon.svg" alt="icon" width="160" height="160">
  </a>

  <h3 align="center">incase</h3>

  <p align="center">
    A word case management library with too many features (just in case).
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Incase is a library to help manage word case. It includes a class for abstracting away from case for easy comparison of words or conversion to any case.
Incase also includes a flexible decorator for managing the case of keywords, inputs, and outputs from functions.

Currently, incase supports the following cases: 
caseless, camel, dromedary, medial, snake, pascal, initial_capitals, kebab, dash, upper_snake, uppercase, upper, lowercase, lower, title, alternating, sarcasm, original, word

If you are aware of another case, please open an issue so we can add it!



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installing with pip

  ```sh
  pip install incase
  ```

For information about cloning and dev setup see: [Contributing](#Contributing)


<!-- USAGE EXAMPLES -->
## Usage

### CLI
You can leverage incase in shell scripts or other non-python contexts by calling it from the cli.
Example:


The default output is snake case.
``` shell
$ incase someCamel
some_camel
```

Use the --case option to set output case
``` shell
$ incase someCamel --case lower
some camel
```

### Caseless
Here is an example showing basic usage of the Caseless class.

```python
{{caseless_example}}
```

### Helper functions

case_modifier is a function for altering other functions. It can change the incoming case of parameter values, the case of the keywords provided, or the case of the function output.
```python
{{case_modifier_example}}
```

Finally, incase is a powerful case coercion function.
```python
{{incase_example}}
```

### Planetary Defense Shield

Note that this is probably not a good idea. However, if you want to be able to easily access objects in globals() by a case other then the one they have, you can use the planetary defense shield.

```python
{{pds_example}}
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Add tests, we aim for 100% test coverage [Using Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/#using-coverage-py)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Cloning / Development setup
1. Clone the repo and install
    ```sh
    git clone https://github.com/kajuberdut/incase.git
    cd incase
    pipenv install --dev
    ```
2. Run tests
    ```sh
    pipenv shell
    ward
    ```
  For more about pipenv see: [Pipenv Github](https://github.com/pypa/pipenv)



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Patrick Shechet - patrick.shechet@gmail.com

Project Link: [https://github.com/kajuberdut/incase](https://github.com/kajuberdut/incase)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kajuberdut/incase.svg?style=for-the-badge
[contributors-url]: https://github.com/kajuberdut/incase/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kajuberdut/incase.svg?style=for-the-badge
[forks-url]: https://github.com/kajuberdut/incase/network/members
[stars-shield]: https://img.shields.io/github/stars/kajuberdut/incase.svg?style=for-the-badge
[stars-url]: https://github.com/kajuberdut/incase/stargazers
[issues-shield]: https://img.shields.io/github/issues/kajuberdut/incase.svg?style=for-the-badge
[issues-url]: https://github.com/kajuberdut/incase/issues
[license-shield]: https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge
[license-url]: https://github.com/kajuberdut/incase/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/patrick-shechet
