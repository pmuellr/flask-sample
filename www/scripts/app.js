$(onLoad)

var lastSeen = -1

//------------------------------------------------------------------------------
function onLoad() {
  uiLog("loaded")
  setInterval(refreshData,      300)
  setInterval(generateNewData, 1000)
}

//------------------------------------------------------------------------------
function uiLog(string) {
  $("#console").append(string + "\n")
}

//------------------------------------------------------------------------------
function refreshData() {
  $.ajax("/api/data", {
    dataType: "json",
    success:  refreshSuccess,
    error:    refreshError
  })
}

//------------------------------------------------------------------------------
function refreshSuccess(data, status, jqXHR) {
  //uiLog("refreshData: " + JSON.stringify(data))
  if (!data) return

  var items = data.data
  if (!items) return

  var foundSome = false
  for (var i=0; i< items.length; i++) {
    var item = items[i]
    if (item.index <= lastSeen) continue

    lastSeen  = item.index
    foundSome = true
    uiLog("got " + item.datum)
  }

  if (!foundSome) {
    uiLog("no new items")
  }
}

//------------------------------------------------------------------------------
function refreshError(jqXHR, status, error) {
  console.log("error refreshing: ", error)
}

//------------------------------------------------------------------------------
function generateNewData() {
  $.ajax("/api/data", {
    method:   "POST",
    data: {
      datum: JSON.stringify("" + new Date())
    },
    dataType: "json",
    success:  generateSuccess,
    error:    generateError
  })
}

//------------------------------------------------------------------------------
function generateSuccess(data, status, jqXHR) {
  // uiLog("generateNewData: " + JSON.stringify(data))
}

//------------------------------------------------------------------------------
function generateError(jqXHR, status, error) {
  console.log("error refreshing: ", error)
}
