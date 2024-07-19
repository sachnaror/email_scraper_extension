chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if (changeInfo.status === 'complete' && tab.url) {
    chrome.tabs.executeScript(tabId, { file: "content.js" });
  }
});
