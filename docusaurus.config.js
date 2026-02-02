// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');
const importPlugin = require('remark-import-partial');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'ITsMagic',
  tagline: 'We Made The Impossible',
  url: 'https://itsmagic.com.br',
  baseUrl: '/documentation/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'ITsMagic', // Usually your GitHub org/user name.
  projectName: 'ITsMagic', // Usually your repo name.

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          remarkPlugins: [importPlugin],
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],
  plugins: [
    [
      require.resolve('@cmfcmf/docusaurus-search-local'),
      {
        indexDocs: true,
        indexPages: false,
        indexBlog: false,
        language: ['en', 'pt'],
      },
    ],
  ],
  i18n: {
      defaultLocale: 'en',
      locales: ['en', 'pt'],
      localeConfigs: {
          en: {
              htmlLang: 'en-GB',
              direction: 'ltr',
          },
          // You can omit a locale (e.g. fr) if you don't need to override the defaults
          pt: {
              direction: 'ltr',
          },
      },
  },

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'ITsMagic Documentation',
        logo: {
          alt: 'ITsMagic Documentation Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Documentation',
          },
          {
            type: 'localeDropdown',
            position: 'left',
          },
          /*{
            to: '/store',
            label: 'Store',
            position: 'left'
          },*/
          {
            href: 'https://play.google.com/store/apps/details?id=com.itsmagic.enginestable',
            label: 'Download',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Documentation',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.gg/64wdG6gZdx',
              },
              {
                label: 'Whatsapp',
                href: 'https://chat.whatsapp.com/Ctgdap8YVRs07QfNaGvLLJ',
              },
            ],
          },
          {
            title: 'More',
            items: [
              /*{
                label: 'Blog',
                to: '/blog',
              },*/
              {
                label: 'Download',
                href: 'https://play.google.com/store/apps/details?id=com.itsmagic.enginestable',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} ITsMagic Engine, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
