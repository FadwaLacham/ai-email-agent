import { useEffect, useState } from "react";

import Card from "@mui/material/Card";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

import DataTable from "examples/Tables/DataTable";

import axios from "axios";

function RecentEmails() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/recent")

      .then((response) => {
        setEmails(response.data);
      })

      .catch((error) => {
        console.log(error);
      });
  }, []);

  const columns = [
    {
      Header: "Sender",
      accessor: "sender",
    },

    {
      Header: "Subject",
      accessor: "subject",
    },

    {
      Header: "Priority",
      accessor: "priority",
    },

    {
      Header: "Decision",
      accessor: "decision",
    },
  ];

  const rows = emails.map((email) => ({
    sender: email.sender,

    subject: email.subject,

    priority: email.priority,

    decision: email.decision,
  }));

  return (
    <Card>
      <MDBox p={3}>
        <MDTypography variant="h6">Recent Emails</MDTypography>
      </MDBox>

      <DataTable
        table={{
          columns,

          rows,
        }}
        entriesPerPage={false}
        showTotalEntries={false}
      />
    </Card>
  );
}

export default RecentEmails;
