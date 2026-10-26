const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 3 });
  await p.goto('file://' + __dirname + '/flyer.html');
  await p.screenshot({ path: 'flyer.png' });
  await p.pdf({ path: 'flyer.pdf', width: '8.5in', height: '11in', printBackground: true });
  await b.close();
})();
