import { useEffect, useState } from "react";
import api from "api/axios";

import Grid from "@mui/material/Grid";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

import ComplexStatisticsCard from "examples/Cards/StatisticsCards/ComplexStatisticsCard";

import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";

import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";

function Analytics() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/analytics")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  if (!data) {
    return (
      <DashboardLayout>
        <DashboardNavbar />

        <MDBox py={3}>Loading...</MDBox>
      </DashboardLayout>
    );
  }

  const priorityData = [
    {
      name: "High",
      value: data.high_priority,
    },

    {
      name: "Medium",
      value: data.medium_priority,
    },

    {
      name: "Low",
      value: data.low_priority,
    },
  ];

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox py={3}>
        <Grid container spacing={3}>
          {/* Total emails */}

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="info"
              icon="email"
              title="Total Emails"
              count={data.total_emails}
              percentage={{
                color: "success",
                amount: "+5%",
                label: "this month",
              }}
            />
          </Grid>

          {/* Success rate */}

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="success"
              icon="check_circle"
              title="Success Rate"
              count={`${data.success_rate}%`}
              percentage={{
                color: "success",
                amount: "",
                label: "processed successfully",
              }}
            />
          </Grid>

          {/* Processing time */}

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="warning"
              icon="timer"
              title="Avg Processing Time"
              count={`${data.average_processing_time}s`}
              percentage={{
                color: "success",
                amount: "",
                label: "average",
              }}
            />
          </Grid>

          {/* Errors */}

          <Grid item xs={12} md={3}>
            <ComplexStatisticsCard
              color="error"
              icon="error"
              title="Errors"
              count={data.errors}
              percentage={{
                color: "error",
                amount: "",
                label: "failed processes",
              }}
            />
          </Grid>
        </Grid>

        <MDBox mt={4}>
          <Grid container spacing={3}>
            {/* Priority chart */}

            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <MDTypography variant="h6">Email Priority Distribution</MDTypography>

                  <ResponsiveContainer width="100%" height={300}>
                    <PieChart>
                      <Pie
                        data={priorityData}
                        dataKey="value"
                        nameKey="name"
                        cx="50%"
                        cy="50%"
                        outerRadius={100}
                        label
                      >
                        {priorityData.map((entry, index) => (
                          <Cell key={index} />
                        ))}
                      </Pie>

                      <Tooltip />
                    </PieChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </Grid>

            {/* AI Statistics */}

            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <MDTypography variant="h6">AI Agent Performance</MDTypography>

                  <MDBox mt={2}>
                    <p>
                      🤖 Top Category :<b>{data.top_category}</b>
                    </p>

                    <p>
                      ⚡ Best Action :<b>{data.top_action}</b>
                    </p>

                    <p>
                      📈 Accuracy :<b>{data.success_rate}%</b>
                    </p>
                  </MDBox>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </MDBox>
      </MDBox>
    </DashboardLayout>
  );
}

export default Analytics;
