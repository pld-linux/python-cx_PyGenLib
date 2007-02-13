%define	module	cx_PyGenLib
Summary:	Generic Python modules used by Computronix projects
Summary(pl.UTF-8):	Podstawowe moduły Pythona wykorzystywane w projektach Computroniksa
Name:		python-%{module}
Version:	2.2
Release:	1
License:	BSD
Vendor:		Anthony Tuininga <anthony@computronix.com>
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/cx-freeze/%{module}-%{version}.tar.gz
# Source0-md5:	8bccc5a5d96bbe5d79d94443c1af8a24
URL:		http://www.computronix.com/utilities.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project contains a number of generic Python modules that are used
by Computronix for a number of projects (cx_Freeze, cx_OracleTools,
cx_OracleDBATools, etc.) and as such they are handled independently,
rather than bundled with the distribution of the dependent project.

%description -l pl.UTF-8
Ten projekt zawiera sporo podstawowych modułów Pythona, które są
wykorzystywane przez wiele projektów Computroniksa (cx_Freeze,
cx_OracleTools, cx_OracleDBATools i in.), którymi można się posługiwać
niezależnie i dla których nie ma powodu pakowania ich łącznie z
odpowiednimi projektami.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

# check-files shutup
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

# this modules are in standard Python 2.3 distribution
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/{modulefinder,textwrap,_strptime,optparse,tarfile}.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt HISTORY.txt
%{py_sitescriptdir}/cx_*.py?
