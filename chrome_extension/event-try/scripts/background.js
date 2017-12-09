chrome.runtime.onStartup.addListener(() => {
  console.log("onStartup");
  run();
});

chrome.tabs.onCreated.addListener((tab) => {
  console.log(`onCreated: ${tab}`);
  run();
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  console.log(`onUpdated and url complete: ${changeInfo.url}, ${changeInfo.status}`);
  if (changeInfo.url) {
    run();
  }
});

chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
  console.log(`onRemoved: ${tabId}, ${removeInfo}`);
  run();
});

chrome.tabs.onReplaced.addListener((addedTabId, removedTabId) => {
  console.log(`onReplaced: ${addedTabId}, ${removedTabId}`);
  run();
});

function run(){
  console.log("run() called!!!!");
  chrome.tabs.query({}, (tabs) => {
    let tabUrls = tabs.map(tab => tab.url);
    console.log(`Tabs: ${tabUrls}`)
  })
}
