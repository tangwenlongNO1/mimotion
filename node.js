const axios = require('axios');

async function getUpdateInfo() {
  console.log('Checking for updates...');
  const response = await axios.get('https://api.github.com/repos/Fndroid/clash_for_windows_pkg/releases/latest');

  return {
    name: response.data.name,
    version: response.data.tag_name,
    url: response.data.assets[0].browser_download_url,
    changelog: response.data.body,
  };
}

getUpdateInfo().then(info => {
  console.log(info);
});

