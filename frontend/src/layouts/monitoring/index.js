import { useEffect, useState } from "react";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

import api from "api/axios";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

import ComplexStatisticsCard from "examples/Cards/StatisticsCards/ComplexStatisticsCard";

function Monitoring() {
  const [monitoring, setMonitoring] = useState(null);

  useEffect(() => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/monitoring")

      .then((response) => {
        setMonitoring(response.data);
      })

      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox py={3}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={3}>
            <ComplexStatisticsCard
              color="success"
              icon="smart_toy"
              title="Agent Status"
              count={monitoring ? monitoring.status : "Loading..."}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={3}>
            <ComplexStatisticsCard
              color="info"
              icon="email"
              title="Processed Emails"
              count={monitoring ? monitoring.processed_emails : 0}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={3}>
            <ComplexStatisticsCard
              color="warning"
              icon="bolt"
              title="Processing Time"
              count={monitoring ? monitoring.processing_time : "0s"}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={3}>
            <ComplexStatisticsCard
              color="dark"
              icon="history"
              title="Last Action"
              count={monitoring ? monitoring.last_action : "None"}
            />
          </Grid>
        </Grid>

        <MDBox mt={4}>
          <Card>
            <MDBox p={3}>
              <MDTypography variant="h6">Last Scan</MDTypography>

              <MDTypography variant="button">
                {monitoring ? monitoring.last_scan : "Loading..."}
              </MDTypography>
            </MDBox>
          </Card>
        </MDBox>
      </MDBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Monitoring;
