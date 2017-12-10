const baseBookmarkDirectoryName = "EventPageExample";

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

async function run(){
  console.log("run() called!!!!");
  const allTabs = await getAllTabs();

  let tabUrls = allTabs.map(tab => tab.url);
  console.log(`Tabs: num: ${tabUrls.length}, ${tabUrls}`);

  const bookmarkTree = await getBookmarkTree();
  console.log(`${bookmarkTree.id}`)

  let baseBookmarkDirectory = getChildDirectory(bookmarkTree, baseBookmarkDirectoryName);
  if (!baseBookmarkDirectory) {
    baseBookmarkDirectory = await createDirectory(bookmarkTree, baseBookmarkDirectoryName)
  }

  for (let tab of allTabs) {
    await createBookmark(baseBookmarkDirectory, tab.title, tab.url)
  }
}

function getChildDirectory(parentDirectory, name) {
  if (!parentDirectory.children) {
    return null;
  }
  for (let i of parentDirectory.children) {
    if (i.url) {
      continue;
    }
    if (i.title == name) {
      return i;
    }
  }
  return null;
}

//Promise
function createDirectory(parentDirectory, name) {
  console.log(parentDirectory.id)
  return new Promise(ok => {
    chrome.bookmarks.create({
      parentId: parentDirectory.id,
      title: name,
      url: null
    }, r => {
      ok(r);
    });
  })
}

function createBookmark(parentDirectory, title, url) {
  return new Promise((resolve, reject) => {
    chrome.bookmarks.create({
      parentId: parentDirectory.id,
      title: title,
      url: url
    }, r => {
      resolve(r);
    });
  });
}

function getBookmarkTree(){
  return new Promise((resolve, reject) => {
    chrome.bookmarks.getTree(r => {
      if (isVivaldi()) {
        return resolve(r[0].children[0])
      } else {
        return resolve(r[0])
      }
    });
  });
}

function getAllTabs(){
  return new Promise(ok => {
    chrome.tabs.query({}, r =>{
      ok(r);
    })
  });
}

function isVivaldi(){
  return navigator.appVersion.match(/Vivaldi/);
}
