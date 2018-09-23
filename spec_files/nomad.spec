%undefine _disable_source_fetch
%define debug_package %{nil}
Name:           nomad
Version:        jeff
Release:        8.5
Summary:        nomad scheduler

Group:          nomad_cloud
BuildArch:      x86_64
License:        MPL2
URL:            https://www.nomadproject.io/
Source0:        https://releases.hashicorp.com/nomad/0.8.5/nomad_0.8.5_linux_amd64.zip
Source1:        https://github.com/hashicorp/nomad/raw/master/dist/systemd/nomad.service


%description
Scheduler for various environments including nomad

%prep
%setup -q -c -n builddir
%build
%install
cp %{_sourcedir}/nomad.service %{_builddir}/builddir
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 nomad $RPM_BUILD_ROOT/usr/bin/nomad
install -m 0755 -d $RPM_BUILD_ROOT/etc/nomad
install -m 0755 -d $RPM_BUILD_ROOT/etc/systemd/system
install -m 0644 nomad.service $RPM_BUILD_ROOT/etc/systemd/system/nomad.service

%files
/usr/bin/nomad
/etc/nomad
/etc/systemd/system/nomad.service

%pre
getent group nomad >/dev/null || groupadd -r nomad
getent passwd nomad >/dev/null || \
    useradd -r -g nomad -d /home/nomad -s /sbin/nologin \
    -c "Nomad user" nomad
exit 0

%changelog
