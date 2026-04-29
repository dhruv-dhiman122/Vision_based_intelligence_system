// ── Color Scheme ─────────────────────────────────────────────────────────────
const chartColors = {
  primary: "#2563eb",
  secondary: "#10b981",
  warning: "#f59e0b",
  danger: "#ef4444",
  purple: "#a855f7",
  pink: "#ec4899",
};

// ── Chart instances ───────────────────────────────────────────────────────────
let congestionChart, flowChart, speedChart, densityChart;

// ── Chart initialisation ──────────────────────────────────────────────────────
function initializeCharts() {
  // Chart 1 — Congestion Level by Hour
  congestionChart = new Chart(
    document.getElementById("congestionChart").getContext("2d"),
    {
      type: "line",
      data: {
        labels: [
          "6 AM",
          "7 AM",
          "8 AM",
          "9 AM",
          "10 AM",
          "11 AM",
          "12 PM",
          "1 PM",
          "2 PM",
          "3 PM",
          "4 PM",
          "5 PM",
        ],
        datasets: [
          {
            label: "Congestion Level (%)",
            data: [15, 35, 72, 85, 78, 65, 45, 38, 42, 55, 68, 82],
            borderColor: chartColors.danger,
            backgroundColor: "rgba(239,68,68,0.1)",
            borderWidth: 3,
            fill: true,
            tension: 0.4,
            pointRadius: 5,
            pointBackgroundColor: chartColors.danger,
            pointBorderColor: "#fff",
            pointBorderWidth: 2,
            pointHoverRadius: 7,
          },
        ],
      },
      options: darkChartOptions({ yMax: 100 }),
    },
  );

  // Chart 2 — Vehicle Flow Rate
  flowChart = new Chart(document.getElementById("flowChart").getContext("2d"), {
    type: "bar",
    data: {
      labels: [
        "Main St",
        "Oak Ave",
        "Elm Street",
        "Pine Rd",
        "Maple Dr",
        "Cedar Ln",
      ],
      datasets: [
        {
          label: "Vehicles/Hour",
          data: [2400, 3200, 1800, 2800, 3500, 2100],
          backgroundColor: [
            "rgba(37,99,235,0.8)",
            "rgba(16,185,129,0.8)",
            "rgba(245,158,11,0.8)",
            "rgba(168,85,247,0.8)",
            "rgba(236,72,153,0.8)",
            "rgba(14,165,233,0.8)",
          ],
          borderRadius: 6,
          borderSkipped: false,
        },
      ],
    },
    options: darkChartOptions(),
  });

  // Chart 3 — Speed Distribution
  speedChart = new Chart(
    document.getElementById("speedChart").getContext("2d"),
    {
      type: "doughnut",
      data: {
        labels: ["0-20 km/h", "20-40 km/h", "40-60 km/h", "60+ km/h"],
        datasets: [
          {
            data: [25, 35, 30, 10],
            backgroundColor: [
              chartColors.danger,
              chartColors.warning,
              chartColors.primary,
              chartColors.secondary,
            ],
            borderColor: "#1e293b",
            borderWidth: 2,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            labels: { color: "#f1f5f9", font: { size: 12 } },
            position: "bottom",
          },
          tooltip: {
            callbacks: { label: (ctx) => ctx.label + ": " + ctx.parsed + "%" },
          },
        },
      },
    },
  );

  // Chart 4 — Traffic Density Radar
  densityChart = new Chart(
    document.getElementById("densityChart").getContext("2d"),
    {
      type: "radar",
      data: {
        labels: [
          "Downtown",
          "North Zone",
          "South Zone",
          "East Zone",
          "West Zone",
          "Central",
        ],
        datasets: [
          {
            label: "Traffic Density Index",
            data: [85, 65, 45, 72, 58, 88],
            borderColor: chartColors.primary,
            backgroundColor: "rgba(37,99,235,0.2)",
            borderWidth: 2,
            pointBackgroundColor: chartColors.primary,
            pointBorderColor: "#fff",
            pointBorderWidth: 2,
            pointRadius: 4,
            pointHoverRadius: 6,
            fill: true,
            tension: 0.4,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: { labels: { color: "#f1f5f9", font: { size: 12 } } },
        },
        scales: {
          r: {
            beginAtZero: true,
            max: 100,
            grid: { color: "rgba(255,255,255,0.1)" },
            ticks: { color: "#cbd5e1", stepSize: 20 },
            pointLabels: { color: "#cbd5e1", font: { size: 12 } },
          },
        },
      },
    },
  );
}

// Helper: shared dark-theme chart options
function darkChartOptions({ yMax } = {}) {
  const yScale = {
    grid: { color: "rgba(255,255,255,0.1)" },
    ticks: { color: "#cbd5e1" },
  };
  if (yMax) {
    yScale.beginAtZero = true;
    yScale.max = yMax;
  }
  return {
    responsive: true,
    maintainAspectRatio: true,
    plugins: { legend: { labels: { color: "#f1f5f9", font: { size: 12 } } } },
    scales: {
      y: yScale,
      x: {
        grid: { color: "rgba(255,255,255,0.1)" },
        ticks: { color: "#cbd5e1" },
      },
    },
  };
}

// ── Query submit (charts update) ──────────────────────────────────────────────
function submitQuery() {
  const location = document.getElementById("location").value.trim();
  const timeRange = document.getElementById("time-range").value;
  const metric = document.getElementById("metric").value;

  if (!location) {
    alert("Please enter a location");
    return;
  }

  updateChartsData(metric);
  showNotification(
    `Analyzing traffic for ${location} (${timeRange})`,
    "success",
  );
}

function updateChartsData(metric) {
  const rand = (min, max) => Math.random() * (max - min) + min;

  switch (metric) {
    case "congestion":
      congestionChart.data.datasets[0].data = Array.from({ length: 12 }, () =>
        Math.round(rand(10, 95)),
      );
      congestionChart.update();
      break;
    case "flow":
      flowChart.data.datasets[0].data = Array.from({ length: 6 }, () =>
        Math.round(rand(1500, 4000)),
      );
      flowChart.update();
      break;
    case "speed":
      speedChart.data.datasets[0].data = [20, 30, 35, 15];
      speedChart.update();
      break;
    case "density":
      densityChart.data.datasets[0].data = Array.from({ length: 6 }, () =>
        Math.round(rand(20, 100)),
      );
      densityChart.update();
      break;
  }
  updateLastUpdateTime();
}

// ── Live stats from /stats ────────────────────────────────────────────────────
async function fetchLiveStats() {
  try {
    const res = await fetch("/stats");
    if (!res.ok) return;
    const data = await res.json();

    // Sidebar badges next to the video feed
    const count = data.total_vehicles ?? "—";
    const level = data.traffic_level ?? "—";
    document.getElementById("live-count").textContent = count;
    document.getElementById("live-level").textContent = level;

    // Bottom stats section
    document.getElementById("stat-total").textContent = count;
    document.getElementById("stat-level").textContent = level;
  } catch (_) {
    /* server may not be running yet — ignore */
  }
}

// ── News feed from /reports ───────────────────────────────────────────────────
async function fetchReports() {
  try {
    const res = await fetch("/reports");
    if (!res.ok) return;
    const reports = await res.json();
    renderNewsFeed(reports);
  } catch (_) {
    /* fallback: show static placeholder items */
  }
}

function renderNewsFeed(reports) {
  const feed = document.getElementById("news-feed");
  if (!reports || reports.length === 0) {
    feed.innerHTML =
      '<p style="color:var(--text-secondary); font-size:0.9rem;">No reports yet.</p>';
    return;
  }
  feed.innerHTML = reports
    .map((r) => {
      const severity = (r.severity || "low").toLowerCase();
      const cls =
        severity === "high"
          ? "alert"
          : severity === "medium"
            ? "warning"
            : "info";
      const ts = r.timestamp
        ? new Date(r.timestamp).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })
        : "Just now";
      return `
        <div class="news-item ${cls}">
            <span class="time-badge">${ts}</span>
            <h4>${r.title || "📍 Community Report"}</h4>
            <p>${r.message || ""}</p>
            <span class="severity">Severity: ${severity.charAt(0).toUpperCase() + severity.slice(1)}</span>
        </div>`;
    })
    .join("");
}

// ── Submit a community report ─────────────────────────────────────────────────
async function submitReport() {
  const location = document.getElementById("report-location").value.trim();
  const message = document.getElementById("report-message").value.trim();

  if (!location || !message) {
    alert("Please fill in both location and message.");
    return;
  }
  try {
    const res = await fetch("/report", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ location, message }),
    });
    if (res.ok) {
      document.getElementById("report-location").value = "";
      document.getElementById("report-message").value = "";
      showNotification("Report submitted successfully!", "success");
      fetchReports(); // refresh news feed
    }
  } catch (_) {
    showNotification(
      "Could not submit report. Is the server running?",
      "error",
    );
  }
}

// ── Chatbot ───────────────────────────────────────────────────────────────────
async function sendChat() {
  const input = document.getElementById("chat-input");
  const message = input.value.trim();
  if (!message) return;

  appendChatBubble(message, "user");
  input.value = "";

  // Optimistic "typing" indicator
  const typingId = "typing-" + Date.now();
  appendChatBubble("…", "bot", typingId);

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    document.getElementById(typingId)?.remove();
    appendChatBubble(data.response || "No response received.", "bot");
  } catch (_) {
    document.getElementById(typingId)?.remove();
    appendChatBubble(
      "Could not reach the server. Make sure Flask is running.",
      "bot",
    );
  }
}

function appendChatBubble(text, role, id) {
  const win = document.getElementById("chat-window");
  const bubble = document.createElement("div");
  bubble.className = `chat-bubble ${role}`;
  bubble.textContent = text;
  if (id) bubble.id = id;
  win.appendChild(bubble);
  win.scrollTop = win.scrollHeight;
}

// ── Notifications ─────────────────────────────────────────────────────────────
function showNotification(message, type = "info") {
  const n = document.createElement("div");
  n.style.cssText = `
        position:fixed; top:20px; right:20px;
        padding:1rem 1.5rem;
        background:${type === "success" ? "#10b981" : type === "error" ? "#ef4444" : "#2563eb"};
        color:white; border-radius:6px;
        box-shadow:0 4px 12px rgba(0,0,0,0.3);
        z-index:1000; animation:slideIn 0.3s ease-out;`;
  n.textContent = message;
  document.body.appendChild(n);
  setTimeout(() => {
    n.style.animation = "slideOut 0.3s ease-out";
    setTimeout(() => n.remove(), 300);
  }, 3000);
}

// ── Utilities ─────────────────────────────────────────────────────────────────
function updateLastUpdateTime() {
  document.getElementById("last-update").textContent =
    new Date().toLocaleTimeString();
}

// Add slideOut animation
const _style = document.createElement("style");
_style.textContent = `
    @keyframes slideOut { to { opacity:0; transform:translateX(100px); } }
    .chat-bubble { padding:0.6rem 1rem; border-radius:12px; max-width:90%;
                   font-size:0.9rem; line-height:1.5; word-break:break-word; }
    .chat-bubble.user { background:#2563eb; color:#fff; align-self:flex-end;
                        border-bottom-right-radius:3px; }
    .chat-bubble.bot  { background:#1e293b; color:#f1f5f9; align-self:flex-start;
                        border-bottom-left-radius:3px; }
`;
document.head.appendChild(_style);

// ── Export (Ctrl+E) ───────────────────────────────────────────────────────────
function exportTrafficData() {
  const data = {
    timestamp: new Date().toISOString(),
    location: document.getElementById("location").value,
    timeRange: document.getElementById("time-range").value,
    metric: document.getElementById("metric").value,
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `traffic-data-${Date.now()}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

document.addEventListener("keydown", (e) => {
  if (e.ctrlKey && e.key === "e") {
    e.preventDefault();
    exportTrafficData();
  }
});

// ── Boot ──────────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  initializeCharts();
  updateLastUpdateTime();
  fetchReports();
  fetchLiveStats();

  // Refresh live stats every 5 seconds
  setInterval(fetchLiveStats, 5000);
  // Refresh news feed every 30 seconds
  setInterval(fetchReports, 30000);
  // Update timestamp every 30 seconds
  setInterval(updateLastUpdateTime, 30000);
});

// Enter key on chat input
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("chat-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendChat();
  });

  document.getElementById("location").addEventListener("keypress", (e) => {
    if (e.key === "Enter") submitQuery();
  });
});
