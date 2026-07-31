const fs = require('fs');
const path = require('path');

const manifestPath = path.join(__dirname, 'android', 'app', 'src', 'main', 'AndroidManifest.xml');
if (fs.existsSync(manifestPath)) {
    let content = fs.readFileSync(manifestPath, 'utf8');
    if (!content.includes('android:usesCleartextTraffic="true"')) {
        content = content.replace('<application', '<application\n        android:usesCleartextTraffic="true"');
        fs.writeFileSync(manifestPath, content, 'utf8');
        console.log('Successfully injected usesCleartextTraffic="true" into AndroidManifest.xml');
    }
} else {
    console.error('AndroidManifest.xml not found at ' + manifestPath);
}
