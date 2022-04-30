<div align="center" id = "top">
  <img src="logo.png"  alt="roxy logo"/>
  <h3>Deploy Self-Hosted Proxy to unblock websites through Heroku in one click</h3> 
</div>

## Contents
- [Introduction](#introduction)
- [Environment Variables](#environment-variables)
- [One-Click Deploy](#one-click-deploy)
- [Deploy using Local Machine](#deploy-using-local-machine)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Introduction
- Roxy is a simple self-hosted proxy on Heroku to unblock websites
- Complex websites which require various domains to function properly will break as they require indiviually written custom rewrite rules
- Roxy is tested on common websites <sup>read piracy</sup> such as `1337x.to`, `nyaa.si`, `thepiratebay.org` etc.
- Heroku Free dyno auto-sleeps after 20 minutes to prevent that Roxy can keep itself alive but it should be enabled manually through environment variables
## Environment Variables

To deploy and use Roxy the following Environment Variables are required:

- `DOMAIN` - The domain to proxy through heroku ( Only **domain** name e.g. example.com)
    - Note: 
        - If a websites redirects to different domain then redirected domain should be entered.
        - Example: `google.com` will redirect to `www.google.com` then `www.google.com` should be entered as `DOMAIN` 

- `KEEP_DYNO_ALIVE` (Default: `false`) - Should Roxy keep heroku free dyno alive 

- `HEROKU_APP_URL` - Full Heroku App URL (required if `KEEP_DYNO_ALIVE` is `true`)
<p align="right">(<a href="#top">back to top</a>)</p>

## One-Click Deploy
- Click  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/coolfool/roxy)
- Enter the environment variables as explained
- Deploy and Visit the heroku app url 
<p align="right">(<a href="#top">back to top</a>)</p>


## Deploy using Local Machine

1) Clone the project `git clone https://github.com/CoolFool/roxy`
2) Go to the project directory `cd Roxy`
3) Install Heroku CLI and Git for your platform
4) Use the `heroku login` command to log in to the Heroku CLI:
5) Create an app on Heroku using `heroku create` and note the URL Generated
6) Add the required buildpacks as follows:
  - `heroku buildpacks:set heroku/python`
  - `heroku buildpacks:set https://github.com/CoolFool/heroku-buildpack-nginx.git`
7) Set `DOMAIN` environment variable using `heroku config:set DOMAIN=example.org`
8) Heroku Free Dyno sleeps after 20 minutes.<br> 
If you want to keep the Dyno alive set the following environment values using <br>
    - `heroku config:set KEEP_DYNO_ALIVE=true`
    - `heroku config:set HEROKU_APP_URL=https://example-app-123.herokuapp.com` (Set the generated URL as its value)
9) Now deploy Roxy using `git push heroku main`
10) Visit Roxy at the URL generated while creating the app or run `heroku open`
11) View Logs for the app using `heroku logs --tail`
<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


## Authors

- [@coolfool](https://www.github.com/coolfool)

<p align="right">(<a href="#top">back to top</a>)</p>

## License

[MIT](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>
