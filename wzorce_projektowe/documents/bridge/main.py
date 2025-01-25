from abc import ABC, abstractmethod


# --- Implementor: Interfejs eksportu raportu ---
class ReportExporter(ABC):
    @abstractmethod
    def export(self, content):
        pass


# --- ConcreteImplementor: Eksport do PDF ---
class PDFExporter(ReportExporter):
    def export(self, content):
        print(f"Exporting to PDF:\n{content}")


# --- ConcreteImplementor: Eksport do CSV ---
class CSVExporter(ReportExporter):
    def export(self, content):
        print(f"Exporting to CSV:\n{content}")


# --- Abstraction: Raport ---
class Report:
    def __init__(self, exporter: ReportExporter):
        self.exporter = exporter

    @abstractmethod
    def generate_content(self):
        pass

    def export(self):
        content = self.generate_content()
        self.exporter.export(content)


# --- RefinedAbstraction: Raport finansowy ---
class FinancialReport(Report):
    def generate_content(self):
        return "Financial Report Content: Revenue: $1,000,000, Profit: $200,000"


# --- RefinedAbstraction: Raport sprzedaży ---
class SalesReport(Report):
    def generate_content(self):
        return "Sales Report Content: Total Sales: 10,000 units, Top Product: Widget"


# --- Przykład użycia ---
if __name__ == "__main__":
    # Eksporterzy
    pdf_exporter = PDFExporter()
    csv_exporter = CSVExporter()

    # Raport finansowy w formacie PDF
    financial_report_pdf = FinancialReport(pdf_exporter)
    financial_report_pdf.export()

    print("\n")

    # Raport sprzedaży w formacie CSV
    sales_report_csv = SalesReport(csv_exporter)
    sales_report_csv.export()
