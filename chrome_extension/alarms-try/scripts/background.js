chrome.runtime.onStartup.addListener(() => {
  console.log("Alarms try onStartup");
});
chrome.runtime.onInstalled.addListener(() => {
  console.log("Alarms try onInstalled");
  chrome.alarms.create('alarms-try', {
    delayInMinutes: 1.0,
    periodInMinutes: 1.0
  });
});

chrome.alarms.onAlarm.addListener((alarm) => {
  console.log(`onAlarm: ${JSON.stringify(alarm)}`);
  if (alarm.name === "alarms-try") {
    console.log("Alarm called!");
  }
});
