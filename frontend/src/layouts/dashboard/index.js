/**
=========================================================
* Material Dashboard 2 React - AI Email Agent Dashboard
=========================================================
*/

import { useEffect, useState } from "react";

import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";

import MDBox from "components/MDBox";

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

import ReportsBarChart from "examples/Charts/BarCharts/ReportsBarChart";
import ReportsLineChart from "examples/Charts/LineCharts/ReportsLineChart";

import ComplexStatisticsCard from "examples/Cards/StatisticsCards/ComplexStatisticsCard";

import RecentEmails from "layouts/dashboard/components/RecentEmails";

import api from "api/axios";

function Dashboard() {
  const [stats, setStats] = useState(null);

  const [categories, setCategories] = useState([]);

  const [actions, setActions] = useState([]);

  const [performance, setPerformance] = useState(null);

  const [monitoring, setMonitoring] = useState(null);

  const [analytics, setAnalytics] = useState(null);

  const fetchData = () => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/statistics")
      .then((response) => {
        setStats(response.data);
      })
      .catch(console.log);

    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/categories")
      .then((response) => {
        setCategories(response.data);
      })
      .catch(console.log);

    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/actions")
      .then((response) => {
        setActions(response.data);
      })
      .catch(console.log);

    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/performance")
      .then((response) => {
        setPerformance(response.data);
      })
      .catch(console.log);

    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/monitoring")
      .then((response) => {
        setMonitoring(response.data);
      })
      .catch(console.log);

    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/analytics")
      .then((response) => {
        setAnalytics(response.data);
      })
      .catch(console.log);
  };

  useEffect(() => {
    fetchData();

    const interval = setInterval(() => {
      fetchData();
    }, 10000);

    return () => clearInterval(interval);
  }, []);

  const downloadFile = (url, filename) => {
    api
      .get(url, {
        responseType: "blob",
      })

      .then((response) => {
        const fileURL = window.URL.createObjectURL(new Blob([response.data]));

        const link = document.createElement("a");

        link.href = fileURL;

        link.setAttribute("download", filename);

        document.body.appendChild(link);

        link.click();

        link.remove();
      })

      .catch(console.log);
  };

  const categoryChart = {
    labels: categories.map((item) => item.category),

    datasets: {
      label: "Emails",

      data: categories.map((item) => item.count),
    },
  };

  const actionChart = {
    labels: actions.map((item) => item.action),

    datasets: {
      label: "Actions",

      data: actions.map((item) => item.count),
    },
  };

  const priorityChart = {
    labels: performance ? Object.keys(performance.priority_distribution) : [],

    datasets: {
      label: "Priority",

      data: performance ? Object.values(performance.priority_distribution) : [],
    },
  };

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox py={3}>
        {/* ================= EXPORT ================= */}

        <Grid container spacing={3} mb={3}>
          <Grid item xs={12}>
            <Button
              variant="contained"
              color="success"
              onClick={() =>
                downloadFile("https://ai-email-agent-backend.fastapicloud.dev/export/emails/excel", "emails.xlsx")
              }
            >
              📄 Export Excel
            </Button>

            <Button
              variant="contained"
              color="info"
              sx={{ ml: 2 }}
              onClick={() => downloadFile("https://ai-email-agent-backend.fastapicloud.dev/export/emails/pdf", "emails.pdf")}
            >
              📑 Export PDF
            </Button>
          </Grid>
        </Grid>

        {/* ================= STATISTICS ================= */}

        <Grid container spacing={3}>
          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="dark"
              icon="email"
              title="Total Emails"
              count={stats ? stats.total_emails : 0}
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="error"
              icon="priority_high"
              title="High Priority"
              count={stats ? stats.high_priority : 0}
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="warning"
              icon="visibility"
              title="Review"
              count={stats ? stats.medium_priority : 0}
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="success"
              icon="archive"
              title="Archived"
              count={stats ? stats.low_priority : 0}
            />
          </Grid>
        </Grid>

        {/* ================= AI PERFORMANCE ================= */}

        <MDBox mt={4}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard color="success" icon="cloud" title="Uptime" count="99.9%" />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="info"
                icon="speed"
                title="Average Response Time"
                count={analytics ? `${analytics.average_processing_time}s` : "-"}
              />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="warning"
                icon="check_circle"
                title="Success Rate"
                count={analytics ? `${analytics.success_rate}%` : "-"}
              />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="dark"
                icon="psychology"
                title="AI Accuracy"
                count={analytics ? `${analytics.success_rate}%` : "-"}
              />
            </Grid>
          </Grid>
        </MDBox>

        {/* ================= MONITORING ================= */}

        <MDBox mt={4}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="success"
                icon="smart_toy"
                title="Agent Status"
                count={monitoring ? monitoring.status : "Loading"}
              />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="info"
                icon="schedule"
                title="Last Scan"
                count={monitoring ? monitoring.last_scan : "-"}
              />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="warning"
                icon="bolt"
                title="Processing Time"
                count={monitoring ? monitoring.processing_time : "-"}
              />
            </Grid>

            <Grid item xs={12} md={3}>
              <ComplexStatisticsCard
                color="dark"
                icon="psychology"
                title="Last Action"
                count={monitoring ? monitoring.last_action : "-"}
              />
            </Grid>
          </Grid>
        </MDBox>

        {/* ================= CHARTS ================= */}

        <MDBox mt={4.5}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={4}>
              <ReportsBarChart
                color="info"
                title="Emails by Category"
                description="AI classification"
                date=""
                chart={categoryChart}
              />
            </Grid>

            <Grid item xs={12} md={4}>
              <ReportsLineChart
                color="success"
                title="Agent Decisions"
                description="AI actions"
                date=""
                chart={actionChart}
              />
            </Grid>

            <Grid item xs={12} md={4}>
              <ReportsBarChart
                color="warning"
                title="Priority Distribution"
                description="AI priority scoring"
                date=""
                chart={priorityChart}
              />
            </Grid>
          </Grid>
        </MDBox>

        {/* ================= RECENT EMAILS ================= */}

        <MDBox mt={4}>
          <RecentEmails />
        </MDBox>
      </MDBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
